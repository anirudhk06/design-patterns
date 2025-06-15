import threading
from datetime import datetime

class SingletonMeta(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                cls._instance = super().__call__(*args, **kwargs)

        return cls._instance


class Logger(metaclass=SingletonMeta):
    def __init__(self) -> None:
        pass
    
    def log(self, message: str) -> None:
        print(f"[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] {message}")


def main() -> None:
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("Hello")
    logger2.log("Hi")

    print(logger1 is logger2)


if __name__ == "__main__":
    main()
