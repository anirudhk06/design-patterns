from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send(self):
        raise NotImplementedError("sub classes must be implement send() method")


class ScheduleNotification(ABC):
    @abstractmethod
    def schedule(self):
        raise NotImplementedError("sub classes must be implement schedule() method")


class CancelNotification(ABC):
    @abstractmethod
    def cancel(self):
        raise NotImplementedError("sub classes must be implement cancel() method")


class PushNotification(NotificationService, CancelNotification):
    def send(self):
        print("sending notification")

    def cancel(self):
        print("cancelling notification")


class EmailNotification(NotificationService, ScheduleNotification):
    def send(self):
        print("sending notification")

    def schedule(self):
        print("scheduling notification")


class SMSNotification(NotificationService):
    def send(self):
        print("sending notification")
