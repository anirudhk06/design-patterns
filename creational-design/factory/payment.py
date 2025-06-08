from typing import Type


class PaymentService:
    def pay(self) -> None:
        raise NotImplementedError("Subclasses must implement the pay method")


class RazorPay(PaymentService):
    def pay(self) -> None:
        print("Payment is processing via RazorPay")


class ClickPay(PaymentService):
    def pay(self) -> None:
        print("Payment is processing via ClickPay")


class PayPal(PaymentService):
    def pay(self) -> None:
        print("Payment is processing via PayPal")


class PayTab(PaymentService):
    def pay(self) -> None:
        print("Payment is processing via PayTab")


class Upi(PaymentService):
    def pay(self) -> None:
        print("Payment is processing via Upi")


class PaymentFactory:
    _methods: dict[str, Type[PaymentService]] = {
        "razorpay": RazorPay,
        "clickpay": ClickPay,
        "paypal": PayPal,
        "paytab": PayTab,
        "upi": Upi,
    }

    @staticmethod
    def get_payment_method(method: str) -> PaymentService:
        method = method.lower().strip()
        if method not in PaymentFactory._methods:
            raise ValueError("Invalid payment method")
        return PaymentFactory._methods[method]()


def main() -> None:
    payment_process = PaymentFactory.get_payment_method("upi")
    payment_process.pay()


if __name__ == "__main__":
    main()
