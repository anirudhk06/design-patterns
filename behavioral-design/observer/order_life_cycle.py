from abc import ABC, abstractmethod
from enum import Enum


class OrderState(Enum):
    CREATED = "Created"
    PAID = "Paid"
    SHIPPED = "Shipped"


class Observer(ABC):
    @abstractmethod
    def update(self, event: OrderState):
        raise NotImplementedError("Sub classes must be implement update() method")


class EmailObserver(Observer):
    def update(self, event: OrderState):
        print(f"Email: Order {event.value}")


class InventoryObserver(Observer):
    def update(self, event: OrderState):
        if event == OrderState.PAID:
            print(f"Inventory: Reserve stock")


class ShippingObserver(Observer):
    def update(self, event: OrderState):
        if event == OrderState.SHIPPED:
            print(f"Shipping: Ship order")


class OrderService:
    def __init__(self):
        self.subscribers: list[Observer] = []

    def attach(self, subscriber: Observer) -> None:
        if subscriber in self.subscribers:
            return

        self.subscribers.append(subscriber)

    def detach(self, subscriber: Observer) -> None:
        self.subscribers.remove(subscriber)

    def create_order(self):
        self._notify(OrderState.CREATED)

    def pay_order(self):
        self._notify(OrderState.PAID)

    def ship_order(self):
        self._notify(OrderState.SHIPPED)

    def _notify(self, event: OrderState):
        for subscriber in self.subscribers:
            subscriber.update(event)


def main() -> None:
    order = OrderService()
    order.attach(EmailObserver())
    order.attach(InventoryObserver())
    order.attach(ShippingObserver())

    order.create_order()
    order.pay_order()
    order.ship_order()



if __name__ == "__main__":
    main()
