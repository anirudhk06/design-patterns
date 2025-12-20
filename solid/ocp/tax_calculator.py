from abc import ABC, abstractmethod


class TaxInterFace(ABC):
    @abstractmethod
    def calculate_tax(self, price: float):
        raise NotImplementedError(
            "sub classes must be implemented calculate_tax() method"
        )


class India(TaxInterFace):
    def calculate_tax(self, price) -> float:
        return (price * 18) / 100


class UnitedStates(TaxInterFace):
    def calculate_tax(self, price) -> float:
        return (price * 10) / 100


class UnitedKingdom(TaxInterFace):
    def calculate_tax(self, price) -> float:
        return (price * 12) / 100


class CalculateTax:
    def __init__(self, country: TaxInterFace):
        self.country = country

    def calculate_tax(self, price):
        return self.country.calculate_tax(price)


def main():
    tax = CalculateTax(India())
    result = tax.calculate_tax(100)
