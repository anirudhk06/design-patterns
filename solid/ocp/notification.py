from abc import ABC, abstractmethod


class NotificationInterface(ABC):
    @abstractmethod
    def notify(self):
        raise NotImplementedError("sub classes must be implemented notify() method")


class EmailService(NotificationInterface):
    def notify(self):
        print("Sending notification via Email")


class SMSService(NotificationInterface):
    def notify(self):
        print("Sending notification via SMS")


class NotificationService:
    def __init__(self, service: NotificationInterface) -> None:
        self.service = service

    def send(self) -> None:
        self.service.notify()


def main() -> None:
    service = EmailService()
    notification = NotificationService(service)
    notification.send()
