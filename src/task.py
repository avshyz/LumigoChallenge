import time


class Task(object):
    def __init__(self, message):
        self.message = message

    def __call__(self, logger):
        time.sleep(5)
        logger.log(self.message)

    def __str__(self):
        return f"<task: {self.message}>"
