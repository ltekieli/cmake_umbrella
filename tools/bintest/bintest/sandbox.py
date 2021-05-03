import json
import logging
import os
import shlex
from bintest.process import Process


logger = logging.getLogger(__name__)


class BubblewrapSandbox:
    def __init__(self, command, **kwargs):
        self._command = command
        self._process = None
        self._child_pid = None
        self._rc = None

        self._sysroot = kwargs['sysroot'] if 'sysroot' in kwargs else '/'
        self._ro_mountpoints = kwargs['ro_mountpoints'] \
            if 'ro_mountpoints' in kwargs else dict()
        self._rw_mountpoints = kwargs['rw_mountpoints'] \
            if 'rw_mountpoints' in kwargs else dict()

    def _start(self):
        r, w = os.pipe()
        bwrapcmd = [
            "bwrap",
            "--die-with-parent",
            "--unshare-all",
            "--as-pid-1",
            "--info-fd", str(w),
        ]

        if (self._sysroot == '/'):
            bwrapcmd.extend(["--ro-bind", self._sysroot, "/"])
        else:
            bwrapcmd.extend(["--bind", self._sysroot, "/"])
            bwrapcmd.extend(["--dev", "/dev"])
            bwrapcmd.extend(["--proc", "/proc"])
            bwrapcmd.extend(["--tmpfs", "/tmp"])
            bwrapcmd.extend(['--ro-bind', '/bin', '/bin'])
            bwrapcmd.extend(['--ro-bind', '/lib', '/lib'])
            bwrapcmd.extend(['--ro-bind', '/lib64', '/lib64'])
            bwrapcmd.extend(['--ro-bind', '/usr/lib', '/usr/lib'])
            bwrapcmd.extend(['--ro-bind', '/usr/lib64', '/usr/lib64'])

        for source, target in self._rw_mountpoints.items():
            bwrapcmd.extend(['--bind', source, target])

        for source, target in self._ro_mountpoints.items():
            bwrapcmd.extend(['--ro-bind', source, target])

        cmd = bwrapcmd + shlex.split(self._command)

        self._process = Process(cmd, fds=[w])
        self._process.start()

        os.close(w)
        r = os.fdopen(r)
        sandbox_info = r.read()
        r.close()

        j = json.loads(sandbox_info)

        self._child_pid = int(j['child-pid'])

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
        return self._child_pid

    @property
    def rc(self):
        return self._rc
