from abc import ABC, abstractmethod


class LoggingInterface(ABC):
    @abstractmethod
    def log(self):
        raise NotImplementedError("sub classes must be implemented log() method")


class ConsoleLog(LoggingInterface):
    def log(self):
        print("Logging")


class FileLog(LoggingInterface):
    def log(self):
        print("Logging")


def main():
    console_log = ConsoleLog()
    console_log.log()

    file_log = FileLog()
    file_log.log()
