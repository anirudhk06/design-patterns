from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def execute(self, data: str) -> str:
        pass


class OrderService(Service):
    def execute(self, data: str) -> str:
        return f"Order processed for {data}"


class LoggingDecorator(Service):
    def __init__(self, service: Service):
        self.service = service

    def execute(self, data):
        print(f"[LOG] Starting execution with data: {data}")
        result = self.service.execute(data)
        print(f"[LOG] Execution finished with result: {result}")
        return result


def main() -> None:
    service = LoggingDecorator(OrderService())
    result = service.execute("item-123")
    print(result)


if __name__ == "__main__":
    main()
