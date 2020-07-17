import multiprocessing
from queue import Empty


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue: multiprocessing.JoinableQueue, result_queue: multiprocessing.Queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            try:
                task = self.task_queue.get(timeout=10)
                print(f'{proc_name}: {task}')
                answer = task()
                self.task_queue.task_done()
                self.result_queue.put(answer)
            except Empty:
                print(f"${proc_name}: empty queue, exiting")
                return
