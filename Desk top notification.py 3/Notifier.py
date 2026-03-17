from plyer import notification


class Notifier:
    def send(self, title, message, timeout=5):
        notification.notify(
            title=title,
            message=message,
            app_name="Desktop Notifier",
            timeout=timeout
        )