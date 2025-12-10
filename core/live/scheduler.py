import time
from threading import Thread

class Scheduler:
    def __init__(self, interval_seconds=5):
        self.interval = interval_seconds
        self.tasks = []

    def add_task(self, func, *args, **kwargs):
        self.tasks.append((func, args, kwargs))

    def start(self):
        def run_task(task):
            func, args, kwargs = task
            while True:
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    print("⚠️ Task Error:", e)
                time.sleep(self.interval)

        for task in self.tasks:
            t = Thread(target=run_task, args=(task,))
            t.daemon = True
            t.start()

        while True:
            time.sleep(1)
