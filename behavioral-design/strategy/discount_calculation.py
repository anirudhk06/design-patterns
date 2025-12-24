from abc import ABC, abstractmethod


class DiscountInterface(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float:
        raise NotImplementedError("Sub classes must be implement apply() method")


class NoDiscount(DiscountInterface):
    def apply(self, amount: float):
        return amount


class SeasonalDiscount(DiscountInterface):
    def apply(self, amount: float) -> float:
        return amount - (amount * 0.1)


class PremiumCustomerDiscount(DiscountInterface):
    def apply(self, amount: float) -> float:
        return amount - (amount * 0.2)


class PriceCalculator:
    def __init__(self, discount_strategy: DiscountInterface):
        self.discount_strategy = discount_strategy

    def calculate(self, amount: float) -> float:
        return self.discount_strategy.apply(amount)


def main() -> None:
    calculator = PriceCalculator(SeasonalDiscount())
    final_price = calculator.calculate(1000)


if __name__ == "__main__":
    main()
