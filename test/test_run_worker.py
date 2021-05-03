import logging
import os
import time
import pytest
from bintest.sandbox import BubblewrapSandbox


logger = logging.getLogger(__name__)


@pytest.fixture
def worker(install_prefix, tmp_path):
    logger.info(f"Temp path is: {tmp_path}")

    worker_exe = os.path.join(install_prefix, "bin/worker")
    sysroot = tmp_path / 'sysroot'
    tmp = tmp_path / 'tmp'

    os.mkdir(sysroot)
    os.mkdir(tmp)

    with BubblewrapSandbox(worker_exe,
                           sysroot=sysroot,
                           ro_mountpoints={install_prefix: install_prefix},
                           rw_mountpoints={tmp: '/tmp'}) as worker:
        yield worker
    assert worker.rc == 0


def test_run_worker(worker):
    logger.debug(f"Sandbox PID: {worker.ppid}")
    logger.debug(f"Process PID: {worker.pid}")
