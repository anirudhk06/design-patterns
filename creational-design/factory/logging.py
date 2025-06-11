from typing import Type, Any, Optional
from datetime import datetime


class LoggerService:
    def log(self, *args, **kwargs) -> None:
        raise NotImplementedError("Subclasses must be implemented log method")


class ConsoleLogger(LoggerService):
    def log(self, message: str = "") -> None:
        print(f"[Console] {message}")


class FileLogger(LoggerService):
    def log(self, message: str = "") -> None:
        timestamp = datetime.now().strftime("%I:%M:%S %p %d-%M-%Y")
        print(f"[File] {timestamp} - {message}")


class DBLogger(LoggerService):

    def log(self, message: str = "") -> None:
        print(f"[DB] LogEntry: {message}")


class LoggerFactory:
    _methods: dict[str, Type[LoggerService]] = {
        "console": ConsoleLogger,
        "file": FileLogger,
        "db": DBLogger,
    }

    @staticmethod
    def get_logger(method: str = "") -> LoggerService:
        """
        Supported types console, file, db.
        """
        cleaned_method: str = str(method).lower().strip()

        if cleaned_method not in LoggerFactory._methods:
            raise ValueError(
                f"Invalid method of '{method}'. Supported types console, file, db."
            )

        return LoggerFactory._methods[cleaned_method]()


def main() -> None:
    logger = LoggerFactory.get_logger("console")
    logger.log("User login failed")


if __name__ == "__main__":
    main()
