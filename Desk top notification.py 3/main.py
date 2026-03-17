from Notifier import Notifier
from scheduler import Scheduler

notifier = Notifier()
scheduler = Scheduler(notifier)

scheduler.schedule_notification(
    title="Reminder",
    message="This is your desktop notification!",
    interval_seconds=10
)

scheduler.run()