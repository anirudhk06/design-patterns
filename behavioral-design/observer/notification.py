from abc import ABC, abstractmethod


class NotificationStrategy(ABC):
    @abstractmethod
    def send(self):
        raise NotImplementedError("Sub classes must be implement send() method")


class EmailStrategy(NotificationStrategy):
    def send(self):
        print("Sending notification via Email")


class SMSStrategy(NotificationStrategy):
    def send(self):
        print("Sending notification via SMS")


class NotificationObserver:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def update(self, event: str) -> None:
        self.strategy.send(event)


class OrderService:
    def __init__(self):
        self.subscribers: list[NotificationObserver] = []

    def attach(self, subscriber) -> None:
        self.subscribers.append(subscriber)

    def place_order(self) -> None:
        for subscriber in self.subscribers:
            subscriber.update()


def main() -> None:
    order = OrderService()

    order.attach(NotificationObserver(EmailStrategy()))
    order.attach(NotificationObserver(SMSStrategy()))

    order.place_order()


if __name__ == "__main__":
    main()
