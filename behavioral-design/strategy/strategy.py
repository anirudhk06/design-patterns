from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount) -> None:
        raise NotImplementedError(
            "Sub classes must be implement process_payment() method"
        )


class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount) -> None:
        print("Processing credit card")


class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount) -> None:
        print("Processing paypal")


class CryptoPayment(PaymentStrategy):
    def process_payment(self, amount) -> None:
        print("Processing crypto")


class StripePayment(PaymentStrategy):
    def process_payment(self, amount) -> None:
        print("Processing stripe")


class ApplePayment(PaymentStrategy):
    def process_payment(self, amount) -> None:
        print("Processing apple pay")


class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy = payment_strategy

    def process_payment(self, amount) -> None:
        self.payment_strategy.process_payment(amount)

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self.payment_strategy = strategy


class PaymentStrategyFactory:
    _payment_strategies = {
        "paypal": PayPalPayment,
        "crypto": CryptoPayment,
        "stripe": StripePayment,
        "apple_pay": ApplePayment,
        "credit_card": CreditCardPayment,
    }

    @staticmethod
    def create(strategy: str):
        try:
            return PaymentStrategyFactory._payment_strategies[strategy]()
        except KeyError:
            raise ValueError(f"Unsupported payment type: {strategy}")


def main() -> None:
    apple_pay = PaymentStrategyFactory.create("apple_pay")

    payment = PaymentProcessor(apple_pay)
    payment.process_payment(1000)


if __name__ == "__main__":
    main()
