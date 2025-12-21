from abc import ABC, abstractmethod


class PaymentService(ABC):
    @abstractmethod
    def pay(self):
        raise NotImplementedError("subclasses must be implement pay() method")


class ReceiptInterface(ABC):
    @abstractmethod
    def generate(self):
        raise NotImplementedError("subclasses must be implement generate() method")


class CreditCardService(PaymentService):
    def pay(self, amount):
        pass


class UPIService(PaymentService):
    def pay(self, amount):
        pass


class EmailReceipt(ReceiptInterface):
    def generate(self):
        pass


class PDFReceipt(ReceiptInterface):
    def generate(self):
        pass


class PaymentProcessor:
    def __init__(self, payment_method: PaymentService, receipt_type: ReceiptInterface):
        self.payment_method = payment_method
        self.receipt_type = receipt_type

    def process(self, amount: float):
        self.payment_method.pay(amount)
        self.receipt_type.generate()


def main():
    payment = PaymentProcessor(UPIService(), EmailReceipt())
    payment.process(1000)
