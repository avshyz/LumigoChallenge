import multiprocessing
from queue import Empty

from logger import Logger


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue: multiprocessing.Queue, invocation_count, logger: Logger, timeout=10):
        multiprocessing.Process.__init__(self)
        self.timeout = timeout
        self.task_queue = task_queue
        self.logger = logger
        self.invocation_counter = invocation_count

    def run(self):
        proc_name = self.name
        while True:
            try:
                task = self.task_queue.get(timeout=self.timeout)
                print(f'{proc_name}: {task}')
                task(self.logger)
                self.invocation_counter.increment()
            except Empty:
                print(f"${proc_name}: empty queue, exiting")
                return
