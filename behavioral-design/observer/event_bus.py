from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict, List, Type


class Event:
    pass


class OrderPlacedEvent(Event):
    def __init__(self, order_id: int):
        self.order_id = order_id


class OrderCancelledEvent(Event):
    def __init__(self, order_id: int):
        self.order_id = order_id


# subscriber


class Subscriber(ABC):
    @abstractmethod
    def handle(self, event: Event):
        raise NotImplementedError("Sub classes must be implement handle() method")


class EmailSubscriber(Subscriber):
    def handle(self, event: Type[Event]):
        if isinstance(event, OrderPlacedEvent):
            print(f"Email: Order {event.order_id} placed")
        elif isinstance(event, OrderCancelledEvent):
            print(f"Email: Order {event.order_id} cancelled")


class SMSSubscriber(Subscriber):
    def handle(self, event: Type[Event]):
        if isinstance(event, OrderPlacedEvent):
            print(f"SMS: Order {event.order_id} placed")
        elif isinstance(event, OrderCancelledEvent):
            print(f"SMS: Order {event.order_id} cancelled")


class RefundSubscriber(Subscriber):
    def handle(self, event: Event):
        if isinstance(event, OrderCancelledEvent):
            print(f"Refund initiated for order {event.order_id}")


# Event Bus


class EventBus:
    def __init__(self):
        self._subscribers: Dict[Type[Event], List[Subscriber]] = defaultdict(list)

    def subscribe(self, event_type: Type[Event], subscriber: Subscriber):
        if subscriber not in self._subscribers[event_type]:
            self._subscribers[event_type].append(subscriber)

    def publish(self, event: Event):
        for subscriber in self._subscribers[type(event)]:
            subscriber.handle(event)


def main() -> None:
    event_bus = EventBus()

    order1 = OrderPlacedEvent(100)
    order2 = OrderPlacedEvent(101)

    event_bus.subscribe(
        order1, [EmailSubscriber(), SMSSubscriber(), RefundSubscriber()]
    )
    event_bus.subscribe(order2, SMSSubscriber())

    event_bus.publish(order2)


if __name__ == "__main__":
    main()
