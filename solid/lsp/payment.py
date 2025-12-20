from abc import ABC, abstractmethod


class OnlinePaymentService(ABC):
    @abstractmethod
    def pay(self, amount: float):
        raise NotImplementedError("sub classes must be implement pay() method")


class OfflinePaymentService(ABC):
    @abstractmethod
    def collect_amount(self, amount: float):
        raise NotImplementedError("sub classes must be implement pay() method")


class CreditCardPayment(OnlinePaymentService):
    def pay(self, amount):
        print("Paid using credit card.")


class CashPayment(OfflinePaymentService):
    def collect_amount(self, amount):
        print("Collected amount")
