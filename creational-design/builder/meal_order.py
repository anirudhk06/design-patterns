from typing import Optional


class Meal:
    def __init__(self, builder) -> None:
        self.course: str = builder.course
        self.side: Optional[str] = builder.side
        self.drink: Optional[str] = builder.drink
        self.dessert: Optional[str] = builder.dessert
        self.instruction: Optional[str] = builder.instruction

    def get_details(self) -> dict:
        return vars(self)

    def __str__(self) -> str:
        return f"{self.course}"


class MealBuilder:
    def __init__(self) -> None:
        self.course = None
        self.side = None
        self.drink = None
        self.dessert = None
        self.instruction = None

    def set_main_course(self, value: str):
        self.course = value
        return self

    def add_side(self, value: str):
        self.side = value
        return self

    def add_drink(self, value: str):
        self.drink = value
        return self

    def add_dessert(self, value: str):
        self.dessert = value
        return self

    def add_instruction(self, value: str):
        self.instruction = value
        return self

    def build(self) -> Meal:
        if not self.course:
            raise ValueError("Please add the main course.")

        meal = Meal(self)
        self.__init__()
        return meal


class MealDirector:
    def __init__(self, builder: MealBuilder) -> None:
        if not isinstance(builder, MealBuilder):
            raise ValueError("builder must be a MealBuilder instance.")

        self.builder = builder

    def kids_meal(self) -> Meal:
        return (
            self.builder.set_main_course("Nuggets")
            .add_side("Fries")
            .add_drink("Chocolate Milk")
            .add_dessert("Ice Cream")
            .add_instruction("Include a toy")
            .build()
        )

    def family_meal(self) -> Meal:
        return (
            self.builder.set_main_course("Large Pizza")
            .add_side("Large Fries, Onion Rings")
            .add_drink("4 Soft Drinks or 1 Large Bottle")
            .add_dessert("Family-size Brownie")
            .build()
        )


def main() -> None:
    builder = MealBuilder()
    family_pack = MealDirector(builder).family_meal()
    kids = MealDirector(builder).kids_meal()

    print(family_pack.get_details())
    print(kids.get_details())

    custom_pack = (
        builder.set_main_course("Biriyani")
        .add_side("Fries")
        .add_instruction("Please add a extra spoon.")
        .build()
    )
    print(custom_pack.get_details())


if __name__ == "__main__":
    main()
