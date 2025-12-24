from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor


class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, event):
        raise NotImplementedError("Sub classes must be implement send() method")


class EmailStrategy(NotificationStrategy):
    def send(self, event: "Event"):
        print(f"Email: Order {event.order_id} placed.")


class SMSStrategy(NotificationStrategy):
    def send(self, event: "Event"):
        print(f"SMS: {event.order_id} placed.")


class NotificationObserver:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def update(self, event: "Event") -> None:
        self.strategy.send(event)


class ObserverFactory:
    _strategies = {
        "email": EmailStrategy,
        "sms": SMSStrategy,
    }

    @staticmethod
    def create(notification_type) -> NotificationObserver:
        try:
            strategy = ObserverFactory._strategies[notification_type]()
            return NotificationObserver(strategy)
        except KeyError:
            raise ValueError(f"Unsupported notification type: {notification_type}")


class Event(ABC):
    pass


class OrderPlacedEvent(Event):
    def __init__(self, order_id: int = None):
        self.order_id = order_id


class OrderCancelledEvent(Event):
    def __init__(self, order_id: int = None):
        self.order_id = order_id


class OrderService:
    def __init__(self):
        self.subscribers: list[NotificationObserver] = []

    def attach(self, subscriber: NotificationObserver):
        if subscriber in self.subscribers:
            return

        self.subscribers.append(subscriber)

    def detach(self, subscriber: NotificationObserver):
        self.subscribers.remove(subscriber)

    def place_order(self, order_id: int = None):
        if not order_id:
            raise ValueError("Order ID must be provided")

        event = OrderPlacedEvent(order_id)

        with ThreadPoolExecutor() as executor:
            for subscriber in self.subscribers:
                executor.submit(self._safe_notify, subscriber, event)

    def _safe_notify(self, subscriber, event):
        try:
            subscriber.update(event)
        except Exception as e:
            print(f"Observer failed: {e}")


def main() -> None:
    order = OrderService()

    email_observer = ObserverFactory.create("email")
    sms_observer = ObserverFactory.create("sms")

    order.attach(email_observer)
    order.attach(sms_observer)

    order.place_order(order_id=101)


if __name__ == "__main__":
    main()
