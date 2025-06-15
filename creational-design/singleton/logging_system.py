from typing import Any
from datetime import datetime
import threading


class SingletonMeta(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs) -> Any:
        if cls._instance is None:
            with cls._lock:
                cls._instance = super().__call__(*args, **kwargs)
        else:
            new_level = args[0].upper() if args else kwargs.get("level", "INFO").upper()
            if cls._instance.level != new_level:
                raise ValueError(
                    f"Logger is already initialized with level '{cls._instance.level}', cannot reinitialize with '{new_level}'"
                )
        return cls._instance


class Logger(metaclass=SingletonMeta):
    _log_priority = {"DEBUG": 1, "INFO": 2, "ERROR": 3}

    def __init__(self, level: str = "INFO") -> None:
        level = str(level).upper()
        if level not in self._log_priority.keys():
            raise ValueError(f"Invalid log level {level}")

        self.level = level

    def log(self, level: str, message: str) -> None:
        if level not in self._log_priority:
            raise ValueError(f"Invalid log level '{level}'")

        if self._log_priority[level] >= self._log_priority[self.level]:
            timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            print(f"[{level}] {timestamp}: {message}")


def main() -> None:
    logger1 = Logger("DEBUG")
    logger1.log("INFO", "Server started")

    logger2 = Logger("DEBUG")
    logger2.log("ERROR", "Something broke")

    logger3 = Logger("INFO")


if __name__ == "__main__":
    main()
