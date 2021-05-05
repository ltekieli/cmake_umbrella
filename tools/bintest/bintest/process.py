import logging
import psutil
import subprocess
from bintest.logger import AsyncLogger


logger = logging.getLogger(__name__)


class Process:
    def __init__(self, command, fds=None):
        self._command = command
        self._fds = fds
        self._process = None
        self._logger = None
        self._logger_error = None

    def start(self):
        logger.debug(f"Starting process {self._command}")
        self._process = psutil.Popen(self._command,
                                     bufsize=0,
                                     universal_newlines=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
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
