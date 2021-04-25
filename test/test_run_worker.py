import logging
import os
import time
import pytest
from .process import BubblewrapSandbox


logger = logging.getLogger(__name__)


@pytest.fixture
def worker(install_prefix):
    worker_exe = os.path.join(install_prefix, "bin/worker")
    with BubblewrapSandbox(worker_exe) as worker:
        yield worker
    assert worker.rc == 0


def test_run_worker(worker):
    logger.debug(f"Sandbox PID: {worker.ppid}")
    logger.debug(f"Process PID: {worker.pid}")
