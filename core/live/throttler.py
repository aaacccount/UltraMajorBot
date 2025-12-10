import time

class Throttler:
    def __init__(self, min_interval=1.0):
        self.min_interval = min_interval
        self.last_run = 0

    def can_run(self):
        now = time.time()
        if now - self.last_run >= self.min_interval:
            self.last_run = now
            return True
        return False
