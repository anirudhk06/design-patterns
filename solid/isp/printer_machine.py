from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self):
        raise NotImplementedError("subclasses must be implement print() method")


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        raise NotImplementedError("subclasses must be implement scan() method")


class FaxMachine(ABC):
    @abstractmethod
    def fax(self):
        raise NotImplementedError("subclasses must be implement fax() method")


class SimplePrinter(Printer):
    def print(self):
        pass


class SimpleScanner(Scanner):
    def scan(self):
        pass


class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass
