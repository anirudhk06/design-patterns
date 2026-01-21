from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def execute(self, data: str) -> str:
        pass


class UnstableOrderService(Service):
    def execute(self, data):
        import random

        if random.choice([True, False]):
            raise Exception("Temporary failure")

        return f"Order processed for {data}"


class RetryDecorator(Service):
    def __init__(self, service: Service, retries: int = 1):
        self.service = service
        self.retries = retries

    def execute(self, data: str) -> str:
        last_exception = None

        for attempt in range(1, self.retries + 1):
            try:
                result = self.service.execute(data)

                if attempt > 1:
                    print(f"[RETRY] Success on attempt {attempt}")

                return result

            except Exception as e:
                last_exception = e
                print(f"[RETRY] Attempt {attempt} failed: {e}")

        print(f"[RETRY] All {self.retries} attempts failed")
        raise last_exception


def main() -> None:
    service = RetryDecorator(UnstableOrderService(), retries=3)
    print(service.execute("item-123"))


if __name__ == "__main__":
    main()
