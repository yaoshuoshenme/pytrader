import threading
import os
import json
from schedule.task.simple_task import SimpleTask
from apscheduler.schedulers.background import BackgroundScheduler

c_f = os.path.dirname(__file__)
config_file = os.path.join(c_f, os.path.pardir, "task_config.json")

RUNNING_JOB = {}
TASK_TRIGGER_STRATEGIES = {}
ALL_TASK_CLZ = []
event = threading.Event()


def init_task():
    # 初始化配置
    with open(config_file, mode='r') as f:
        config = json.load(f)
        for c in config:
            TASK_TRIGGER_STRATEGIES[c['task_name']] = c


def run_all_task():
    scheduler = BackgroundScheduler()
    scheduler.start()
    """
    trigger: interval, corn, date
    """

    for c in SimpleTask.__subclasses__():
        config = TASK_TRIGGER_STRATEGIES[c.__name__]
        task = c(config['trigger'], config['triggerArgs'])
        job_instance = scheduler.add_job(task.run, trigger=task.trigger, **task.trigger_args)
        RUNNING_JOB[c.__name__] = job_instance

    event.wait()


if __name__ == '__main__':
    init_task()
    run_all_task()
