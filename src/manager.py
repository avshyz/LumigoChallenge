import multiprocessing

from src.consumer import Consumer
from src.logger import Logger
from src.task import Task


class AtomicCounter(object):
    def __init__(self, initval=0):
        self.val = multiprocessing.Value('i', initval)
        self.lock = multiprocessing.Lock()

    def increment(self, delta=1):
        with self.lock:
            self.val.value += delta

    def decrement(self, delta=1):
        with self.lock:
            self.val.value -= delta

    def value(self):
        with self.lock:
            return self.val.value

class Manager:
    def __init__(self, logger: Logger, initial_workers=4):
        self.tasks = multiprocessing.Queue()
        self.logger = logger
        self.invocation_count = AtomicCounter(0)

        num_consumers = initial_workers
        print('Creating %d consumers' % num_consumers)
        self.consumers = [Consumer(self.tasks, self.invocation_count, logger) for _ in range(num_consumers)]

    def start(self):
        for w in self.consumers:
            w.start()

    def enqueue_task(self, task: Task):
        self.tasks.put(task)


if __name__ == '__main__':
    manager = Manager(logger=Logger())
    manager.start()

    for i in range(10):
        manager.enqueue_task(Task(i))
