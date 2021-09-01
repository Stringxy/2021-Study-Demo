from datetime import timedelta
import djcelery
djcelery.setup_loader()

CELERY_IMPORTS = (
    'blog.tasks'
)

CELERY_QUEUES = {
    'schedule_tasks': {
        'exchange': 'schedule_tasks',
        'exchange_type': 'direct',
        'binding_key': 'schedule_tasks'
    },
    'normal_tasks': {
        'exchange': 'normal_tasks',
        'exchange_type': 'direct',
        'binding_key': 'normal_tasks'
    }
}

CELERYBEAT_SCHEDULE = {
    'beatTask':{
        'task': 'beatTaskName',
        'schedule': timedelta(seconds=5),
        'options': {
            'queue': 'schedule_tasks'
        }
    }
}

CELERY_DEFAULT_QUEUE = 'normal_tasks'
# 防止死锁
CELERYD_FORCE_EXECV = True
# 并发worker数量
CELERYD_CONCURRENCY = 4
# 允许重试
CELERY_ACKS_LATE = True
# 每个worker最多执行100个任务 防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 100
# 单个任务最大执行时间，超过kill
CELERYD_TASK_TIME_LIMIT = 12 * 30

BROKER_BACKEND = 'redis'
BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
