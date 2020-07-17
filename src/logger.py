import multiprocessing
import sys


class Logger:

    def __init__(self, file_path: str):
        self._lock = multiprocessing.Lock()
        self.file_path = file_path

    def log(self, message):
        with self._lock:
            print(f'LOGGER: {message}')
            sys.stdout.flush()
            with open(self.file_path, 'a') as f:
                f.write(message + '\n')
