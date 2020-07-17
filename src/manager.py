import multiprocessing

from src.consumer import Consumer
from src.logger import Logger
from src.task import Task


class Manager:
    def __init__(self, logger: Logger, initial_workers=4):
        self.tasks = multiprocessing.JoinableQueue()
        self.results = multiprocessing.Queue()
        self.logger = logger

        num_consumers = initial_workers
        print('Creating %d consumers' % num_consumers)
        self.consumers = [Consumer(self.tasks, logger) for _ in range(num_consumers)]

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

