from datetime import datetime

class Time:

    def __init__(self, max_time):
        self.max_time = max_time

    def ready(self):
        self.start_time = datetime.now()

    def reached_end(self, gen):
        try:
            return (datetime.now() - self.start_time).total_seconds() >= self.max_time
        except:
            print("Ready hasn't been called")
            return True