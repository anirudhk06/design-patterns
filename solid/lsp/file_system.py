from abc import ABC, abstractmethod


class ReadOnlyFile(ABC):
    @abstractmethod
    def read(self):
        raise NotImplementedError("sub classes must be implement read() method")


class WritableFile(ABC):
    @abstractmethod
    def write(self, data):
        raise NotImplementedError("sub classes must be implement write() method")


class File(ReadOnlyFile, WritableFile):
    def read(self):
        pass

    def write(self, data):
        pass
