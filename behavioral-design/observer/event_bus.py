from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Type
import time
from concurrent.futures import ThreadPoolExecutor

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
        time.sleep(3)
        if isinstance(event, OrderPlacedEvent):
            print(f"Email: Order {event.order_id} placed")
        elif isinstance(event, OrderCancelledEvent):
            print(f"Email: Order {event.order_id} cancelled")


class SMSSubscriber(Subscriber):
    def handle(self, event: Type[Event]):
        time.sleep(4)
        if isinstance(event, OrderPlacedEvent):
            print(f"SMS: Order {event.order_id} placed")
        elif isinstance(event, OrderCancelledEvent):
            print(f"SMS: Order {event.order_id} cancelled")


class RefundSubscriber(Subscriber):
    def handle(self, event: Event):
        time.sleep(3)
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

        with ThreadPoolExecutor() as executor:
            for subscriber in self._subscribers[type(event)]:
                executor.submit(self._safe_notify, subscriber, event)

    def _safe_notify(self, subscriber: Subscriber, event:Event):
        try:
            subscriber.handle(event)
        except Exception as e:
            print(f"Observer failed: {e}")

def main() -> None:
    bus = EventBus()

    order1 = OrderPlacedEvent(100)
    bus.subscribe(OrderPlacedEvent, EmailSubscriber())
    bus.subscribe(OrderPlacedEvent, SMSSubscriber())
    bus.subscribe(OrderPlacedEvent, SMSSubscriber())
    bus.subscribe(OrderPlacedEvent, SMSSubscriber())
    bus.subscribe(OrderPlacedEvent, SMSSubscriber())

    start = datetime.now()
    bus.publish(order1)
    time_taken = (datetime.now() - start).total_seconds()
    print(f"Time taken: {time_taken}")


if __name__ == "__main__":
    main()
