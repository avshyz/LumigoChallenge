import multiprocessing
from queue import Empty

from src.logger import Logger


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue: multiprocessing.Queue, invocation_count, logger: Logger):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.logger = logger
        self.invocation_counter = invocation_count

    def run(self):
        proc_name = self.name
        while True:
            try:
                task = self.task_queue.get(timeout=10)
                print(f'{proc_name}: {task}')
                task(self.logger)
                self.invocation_counter.increment()
            except Empty:
                print(f"${proc_name}: empty queue, exiting")
                return
