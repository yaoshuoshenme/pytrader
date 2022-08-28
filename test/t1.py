import datetime
import threading
from apscheduler.schedulers.background import BackgroundScheduler

def job1():
    print('job1')


def job2(x, y):
    print('job2', x, y)


j_scheduler = BackgroundScheduler()
j_scheduler.start()

j_scheduler.add_job(job1, trigger='interval', seconds=2)



event = threading.Event()
event.wait()