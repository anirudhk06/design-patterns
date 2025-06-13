from abc import ABC, abstractmethod
import re


class Notification(ABC):
    @abstractmethod
    def send() -> None:
        pass


class IndiaEmailNotification(Notification):

    def send(self, to: str, message: str) -> None:
        print(f"Sending EMAIL to {to} with message: [INDIA] {message} via Email!")


class IndiaSMSNotification(Notification):

    def send(self, to: str, message: str) -> None:
        print(f"Sending SMS to {to} with message: [INDIA] {message} via SMS!")


class IndiaPushNotification(Notification):

    def send(self, to: str, message: str) -> None:
        print(f"Sending Push to {to} with message: [INDIA] {message} via Push!")


class USAEmailNotification(Notification):

    def send(self, to: str, message: str) -> None:
        print(f"Sending EMAIL to {to} with message: [USA] {message} via Email!")


class USASMSNotification(Notification):

    def send(self, to: str, message: str) -> None:
        print(f"Sending SMS to {to} with message: [USA] {message} via SMS!")


class USAPushNotification(Notification):

    def send(self, to: str, message: str) -> None:
        print(f"Sending Push to {to} with message: [USA] {message} via Push!")


class NotificationFactory:
    @abstractmethod
    def email(self) -> Notification: ...
    @abstractmethod
    def sms(self) -> Notification: ...
    @abstractmethod
    def push(self) -> Notification: ...


class IndiaNotificationFactory(NotificationFactory):
    def __init__(self) -> None:
        print("Region: INDIA")

    def email(self) -> Notification:
        return IndiaEmailNotification()

    def sms(self) -> Notification:
        return IndiaSMSNotification()

    def push(self) -> Notification:
        return IndiaPushNotification()


class USANotificationFactory(NotificationFactory):
    def __init__(self) -> None:
        print("Region: USA")

    def email(self) -> Notification:
        return USAEmailNotification()

    def sms(self) -> Notification:
        return USASMSNotification()

    def push(self) -> Notification:
        return USAPushNotification()


def main() -> None:
    country = input("Chose country (india/usa): ").lower().strip()

    factory: NotificationFactory = None
    match country:
        case "india":
            factory = IndiaNotificationFactory()
        case "usa":
            factory = USANotificationFactory()
        case _:
            raise ValueError("Invalid input. Available countires are 'india/usa'")

    notification_type = (
        input("Please enter notification medium (email/sms/push): ").lower().strip()
    )

    notification: Notification = None
    match notification_type:
        case "email":
            notification = factory.email()
        case "sms":
            notification = factory.sms()
        case "push":
            notification = factory.push()
        case _:
            raise ValueError("Invalid medium. Available medium are 'email/sms/push'")

    receiver_id = input("Please enter the receiver id: ").strip()

    if not receiver_id:
        raise ValueError("Receiver ID must be set.")

    if isinstance(notification, (IndiaEmailNotification, USAEmailNotification)):
        valid = re.match(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", receiver_id
        )
        if not valid:
            raise ValueError("Invalid email ID")

    message: str = input("Please enter the message: ").strip()
    if not message:
        raise ValueError("Please enter the mesage")

    notification.send(receiver_id, message)


if __name__ == "__main__":
    main()
