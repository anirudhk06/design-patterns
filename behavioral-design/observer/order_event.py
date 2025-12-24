from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        raise NotImplementedError("Sub classes must be implement update() method")


class EmailObserver(Observer):
    def update(self, message: str):
        print(f"Email: {message}")


class SMSObserver(Observer):
    def update(self, message: str):
        print(f"SMS: {message}")


class InventoryObserver(Observer):
    def update(self, message: str):
        print(f"Inventory: {message}")


class OrderService:
    def __init__(self):
        self.subscribers: list[Observer] = []

    def attach(self, subscriber: Observer):
        if subscriber in self.subscribers:
            return

        self.subscribers.append(subscriber)
    
    def detach(self, subscriber: Observer):
        self.subscribers.remove(subscriber)


    def place_order(self):
        for subscriber in self.subscribers:
            subscriber.update("Order is placed")


def main() -> None:
    order_service = OrderService()
    order_service.attach(EmailObserver())
    order_service.attach(SMSObserver())
    order_service.attach(InventoryObserver())

    order_service.place_order()



if __name__ == "__main__":
    main()
