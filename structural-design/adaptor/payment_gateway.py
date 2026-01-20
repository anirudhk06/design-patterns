from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class StripeGateway:
    def make_payment(self, amount: float):
        print(f"Stripe payment of {amount}")


class StripeAdapter(PaymentGateway):
    def __init__(self, stripe_gateway: StripeGateway):
        self.stripe_gateway = stripe_gateway

    def process_payment(self, amount: float):
        self.stripe_gateway.make_payment(amount)


class PaypalGateway:
    def pay(self, data: dict):
        print(f"Paypal payment of {data}")


class PaypalAdapter(PaymentGateway):
    def __init__(self, paypal_gateway: PaypalGateway):
        self.paypal_gateway = paypal_gateway

    def process_payment(self, amount: float):
        self.paypal_gateway.pay({"total": amount})


class Client:
    def checkout(self, gateway: PaymentGateway):
        gateway.process_payment(100)


def main() -> None:
    client = Client()
    client.checkout(StripeAdapter(StripeGateway()))
    client.checkout(PaypalAdapter(PaypalGateway()))


if __name__ == "__main__":
    main()
