import multiprocessing

from src.consumer import Consumer
from src.task import Task


class Manager:
    def __init__(self, initial_workers=4):
        self.tasks = multiprocessing.JoinableQueue()
        self.results = multiprocessing.Queue()

        num_consumers = initial_workers
        print('Creating %d consumers' % num_consumers)
        self.consumers = [Consumer(self.tasks, self.results) for i in range(num_consumers)]

    def start(self):
        for w in self.consumers:
            w.start()

    def enqueue_task(self, task: Task):
        self.tasks.put(task)


if __name__ == '__main__':
    manager = Manager()
    manager.start()

    num_jobs = 10
    for i in range(num_jobs):
        manager.enqueue_task(Task(i))

    # self.tasks.join()

    # TODO ADD A LOGGER PROCESS HERE, feeding from the results queue
    while num_jobs:
        result = manager.results.get()
        print('Result:', result)
        num_jobs -= 1
