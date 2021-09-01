from celery.task import Task
import time


class NormalTask(Task):
    def run(self, *args, **kwargs):
        print('start normal task')
        print('args={},kwargs={}'.format(args, kwargs))
        time.sleep(5)
        print('end normal task')

class BeatTask(Task):
    name = 'beatTaskName'
    def run(self, *args, **kwargs):
        print('start beat task')
        print('args={},kwargs={}'.format(args, kwargs))
        time.sleep(2)
        print('end beat task')