import json
import logging
import os
import psutil
import shlex
import subprocess
import threading


class AsyncLogger:
    def __init__(self, fd, tag):
        self._fd = fd
        self._tag = tag
        self._thread = None

    def start(self):
        self._thread = threading.Thread(target=self._log)
        self._thread.start()

    def stop(self):
        self._thread.join()

    def _log(self):
        logger = logging.getLogger(self._tag)
        for line in iter(self._fd.readline, ""):
            logger.info(line.rstrip())


logger = logging.getLogger(__name__)


class Process:
    def __init__(self, command, fds=None):
        self._command = command
        self._fds = fds
        self._process = None
        self._logger = None

    def start(self):
        logger.debug(f"Starting process {self._command}")
        self._process = psutil.Popen(self._command,
                                     bufsize=0,
                                     universal_newlines=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT,
                                     close_fds=True,
                                     pass_fds=self._fds)
        logger.debug(f"Process started PID:{self._process.pid}")
        self._logger = AsyncLogger(
                self._process.stdout,
                f"{self._command[-1]}:{self._process.pid}")
        self._logger.start()

    def _wait(self, timeout=0):
        logger.debug(f"Waiting for process PID:{self._process.pid}")
        rc = self._process.wait(timeout)
        self._logger.stop()
        return rc

    def stop(self):
        try:
            return self._wait(timeout=5)
        except psutil.TimeoutExpired:
            logger.error("Application didn't finish in 5 seconds")

        logger.debug(f"Terminating PID:{self._process.pid}")
        self._process.terminate()
        try:
            return self._wait(timeout=5)
        except psutil.TimeoutExpired:
            logger.error("Application didn't finish "
                         "in 5 seconds after SIGTERM")

        logger.debug(f"Killing PID:{self._sandbox.pid}")
        self._process.kill()
        return self._wait(timeout=5)

    @property
    def pid(self):
        return self._process.pid


class BubblewrapSandbox:
    def __init__(self, command):
        self._command = command
        self._process = None
        self._child = None
        self._rc = None

    def _start(self):
        r, w = os.pipe()
        cmd = [
            "bwrap",
            "--die-with-parent",
            "--ro-bind", "/", "/",
            "--info-fd", str(w),
        ] + shlex.split(self._command)

        self._process = Process(cmd, fds=[w])
        self._process.start()

        os.close(w)
        r = os.fdopen(r)
        sandbox_info = r.read()
        r.close()

        j = json.loads(sandbox_info)

        self._child = psutil.Process(int(j['child-pid']))

    def _stop(self):
        self._rc = self._process.stop()

    def __enter__(self):
        self._start()
        return self

    def __exit__(self, type_, value, traceback):
        self._stop()

    @property
    def ppid(self):
        return self._process.pid

    @property
    def pid(self):
        return self._child.pid

    @property
    def rc(self):
        return self._rc
