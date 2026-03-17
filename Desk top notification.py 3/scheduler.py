import schedule
import time

class Scheduler:
    def __init__(self, notifier):
        self.notifier = notifier

    def schedule_notification(self, title, message, interval_seconds):
        schedule.every(interval_seconds).seconds.do(
            self.notifier.send, title=title, message=message
        )

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


