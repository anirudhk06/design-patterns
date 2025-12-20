class PricingRule:
    def apply(self, price: float) -> float:
        raise NotImplementedError


class RegularPricing(PricingRule):
    def apply(self, price):
        return price


class PremiumDiscount(PricingRule):
    def apply(self, price) -> float:
        return price * 0.9  # 10% discount


class FestivalDiscount(PricingRule):
    def apply(self, price) -> float:
        return price - 200


class PriceCalculator:
    def __init__(self, rules) -> None:
        self.rules = rules

    def calculate(self, base_price):
        price = base_price
        for rule in self.rules:
            price = rule.apply(price)
        return price


class Order:
    def __init__(self, price) -> None:
        self.price = price

class OrderService:
    def __init__(self, price_calculator):
        self.price_calculator = price_calculator

    def process(self, order):
        return self.price_calculator.calculate(order.price)


def main() -> None:
    order = Order(1000)

    calculator = PriceCalculator([RegularPricing()])

    service = OrderService(calculator)
    print(service.process(order))


if __name__ == "__main__":
    main()
