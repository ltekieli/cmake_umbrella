import json
import logging
import os
import psutil
import shlex
from bintest.process import Process


logger = logging.getLogger(__name__)


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
