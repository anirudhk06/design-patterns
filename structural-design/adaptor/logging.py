from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        raise NotImplementedError("Sub classes must be implement log() method")


class FileLogger:
    def write_log(self, message: str):
        print(f"[FILE] {message}")


class CloudLogger:
    def send(self, payload: dict):
        print(f"[CLOUD] {payload}")


class FileLoggerAdapter(Logger):
    def __init__(self, file_logger: FileLogger):
        self.file_logger = file_logger

    def log(self, message: str):
        self.file_logger.write_log(message)


class CloudLoggerAdapter(Logger):
    def __init__(self, cloud_logger: CloudLogger):
        self.cloud_logger = cloud_logger

    def log(self, message: str):
        self.cloud_logger.send({"message": message})


class Client:
    def process(self, logger: Logger):
        logger.log("User registered successfully")


def main() -> None:
    client = Client()

    client.process(FileLoggerAdapter(FileLogger()))
    client.process(CloudLoggerAdapter(CloudLogger()))


if __name__ == "__main__":
    main()
