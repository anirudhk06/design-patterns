from abc import ABC, abstractmethod


class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        raise NotImplementedError("Sub classes must be implement calculate() method")


class StandardShipping(ShippingStrategy):
    def calculate(self, amount: float) -> float:
        return 50


class ExpressShipping(ShippingStrategy):
    def calculate(self, amount: float) -> float:
        return 100 + (amount * 0.05)


class FreeShipping(ShippingStrategy):
    def calculate(self, amount: float) -> float:
        return 0


class ShippingCostCalculator:
    def __init__(self, shipping_strategy: ShippingStrategy):
        self.shipping_strategy = shipping_strategy

    def set_strategy(self, strategy: ShippingStrategy):
        self.shipping_strategy = strategy
    
    def calculate(self, order_amount: float) -> float:
        return self.shipping_strategy.calculate(order_amount)

def main() -> None:
    calculator = ShippingCostCalculator(ExpressShipping())
    cost = calculator.calculate(order_amount=2000)


if __name__ == "__main__":
    main()
