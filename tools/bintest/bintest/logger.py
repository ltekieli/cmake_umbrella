import logging
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
