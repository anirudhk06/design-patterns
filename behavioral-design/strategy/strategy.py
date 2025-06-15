from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self) -> None:
        pass


class CreditCardPayment(PaymentStrategy):
    def process_payment(self) -> None:
        print("Processing credit card")


class PayPalPayment(PaymentStrategy):
    def process_payment(self) -> None:
        print("Processing paypal")


class CryptoPayment(PaymentStrategy):
    def process_payment(self) -> None:
        print("Processing crypto")


class StripePayment(PaymentStrategy):
    def process_payment(self) -> None:
        print("Processing stripe")


class ApplePayment(PaymentStrategy):
    def process_payment(self) -> None:
        print("Processing apple pay")


class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy = payment_strategy

    def process_payment(self) -> None:
        self.payment_strategy.process_payment()

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self.payment_strategy = strategy


def main() -> None:
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    crypto = CryptoPayment()
    stripe = StripePayment()
    apple_pay = ApplePayment()

    payment = PaymentProcessor(apple_pay)
    payment.process_payment()


if __name__ == "__main__":
    main()
