from typing import Type


class NotificationService:
    def send(self) -> None:
        raise NotImplementedError("Subclasses must implement the pay method")


class SMSNotification(NotificationService):
    def send(self, message: str = None) -> None:
        print("Sending notification via SMS")


class EmailNotification(NotificationService):
    def send(self, message: str = None) -> None:
        print("Sending notification via Email")


class PushNotification(NotificationService):
    def send(self, message: str = None) -> None:
        print("Sending notification via Push notification")


class NotificationFactory:
    _methods: dict[str, Type[NotificationService]] = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
    }

    @staticmethod
    def get_notification(method: str = None) -> NotificationService:
        """
        Available services are 'email', 'sms', 'push'
        """
        method = str(method).lower().strip()
        if method not in NotificationFactory._methods:
            raise ValueError("Invalid notification method")

        return NotificationFactory._methods[method]()


def main() -> None:
    notification_process = NotificationFactory()
    notification = notification_process.get_notification("push")
    notification.send("Hi")


if __name__ == "__main__":
    main()
