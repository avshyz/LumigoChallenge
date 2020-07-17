import multiprocessing
import sys


class Logger:

    def __init__(self):
        self._lock = multiprocessing.Lock()

    def log(self, message):
        with self._lock:
            # TODO MAKE ME WRITE TO FILE
            print(f'LOGGER: {message}')
            sys.stdout.flush()
