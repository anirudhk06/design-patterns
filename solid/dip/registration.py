from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self):
        raise NotImplementedError("subclasses must be implement send() method")


class EmailService(Notifier):
    def send(self):
        print("Sending notification via email")


class SMSNotifier(Notifier):
    def send(self):
        print("Sending notification via sms")


class UserRegistrationService:
    def __init__(self, data):
        self.data = data

    def save(self, notification: Notifier):
        # store the values into the DB

        notification.send()


user = UserRegistrationService({"name": "Anirudh", "email": "anirudh@gmail.com"})
user.save(EmailService())
