from abc import ABC, abstractmethod


class Coffie(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class Espresso(Coffie):

    def get_name(self) -> str:
        return "Espresso"

    def get_cost(self) -> float:
        return 100.00


class Late(Coffie):
    def get_name(self) -> str:
        return "Late"

    def get_cost(self) -> float:
        return 80.00


class CoffieDecorator(Coffie):
    def __init__(self, coffie: Coffie):
        self.coffie = coffie

    def get_name(self):
        return self.coffie.get_name()

    def get_cost(self):
        return self.coffie.get_cost()


class MilkDecorator(CoffieDecorator):
    def __init__(self, coffie: Coffie):
        super().__init__(coffie)

    def get_name(self):
        return f"{self.coffie.get_name()} + Milk"

    def get_cost(self):
        return self.coffie.get_cost() + 0.50


class SugarDecorator(CoffieDecorator):
    def __init__(self, coffie: Coffie):
        super().__init__(coffie)

    def get_name(self):
        return f"{self.coffie.get_name()} + Sugar"

    def get_cost(self):
        return self.coffie.get_cost() + 0.2


def main() -> None:
    espresso = Espresso()

    espresso_with_milk = MilkDecorator(espresso)
    espresso_cost = SugarDecorator(espresso_with_milk).get_cost()
    print(f"Cost {espresso_cost}")


if __name__ == "__main__":
    main()
