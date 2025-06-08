from enum import Enum


class TravelPackage:
    def __init__(self, builder) -> None:
        self.destination: str = builder.destination
        self.flight_class: Enum = builder.flight_class
        self.hotel_type: Enum = builder.hotel_type
        self.meal_plan: Enum = builder.meal_plan
        self.transport: Enum = builder.transport
        self.excursions: list[str] = builder.excursions
        self.instruction: str | None = builder.instruction

    def get_details(self) -> dict:
        return vars(self)

    def __str__(self) -> str:
        return f"{self.destination}"

    def __repr__(self) -> str:
        return f"<{self.destination}: {self.flight_class} {self.hotel_type}>"


class TravelPackageBuilder:
    class FlightClass(Enum):
        ECONOMY = "Economy"
        BUSINESS = "Business"
        FIRST_CLASS = "First Class"

    class HotelType(Enum):
        THREE_STAR = "3 Star"
        FIVE_STAR = "5 Star"
        RESORT = "Resort"

    class MealPlan(Enum):
        BREAKFAST = "Breakfast"
        FULL_BOARD = "Full Board"
        NO_MEALS = "No Meals"

    class Transport(Enum):
        BUS = "Bus"
        PRIVATE_CAB = "Private Cab"
        NO_TRANSPORT = "None"

    def __init__(self) -> None:
        self.destination: str = None
        self.flight_class: str = None
        self.hotel_type: str = None
        self.meal_plan: str = self.MealPlan.NO_MEALS.value
        self.transport: str = self.Transport.NO_TRANSPORT.value
        self.excursions: list[str] = []
        self.instruction: str | None = None

    def add_destination(self, value: str):
        self.destination = value
        return self

    def add_flight_class(self, value: str):
        self.flight_class = value
        return self

    def add_hotel_type(self, value: str):
        self.hotel_type = value
        return self

    def add_meal_plan(self, value: str):
        self.meal_plan = value
        return self

    def add_transport(self, value: str):
        self.transport = value
        return self

    def add_excursions(self, value: str):
        self.excursions.append(value)
        return self

    def add_instruction(self, value: str):
        self.instruction = value
        return self

    def build(self) -> TravelPackage:
        if not self.destination:
            raise ValueError("Please enter the destination you need to visit.")

        if not self.flight_class:
            raise ValueError("Please add the flight class.")

        if not self.hotel_type:
            raise ValueError("Please add the hotel type.")

        try:
            self.FlightClass(self.flight_class)
        except:
            raise ValueError(
                f"Please enter the valid Flight Class. eg: {self.FlightClass.ECONOMY.value}, {self.FlightClass.BUSINESS.value}, {self.FlightClass.FIRST_CLASS.value}"
            )

        try:
            self.MealPlan(self.meal_plan)
        except:
            raise ValueError(
                f"Please enter the valid Meal Plan. eg: {self.MealPlan.BREAKFAST.value}, {self.MealPlan.FULL_BOARD.value}, {self.MealPlan.NO_MEALS.value}"
            )

        try:
            self.HotelType(self.hotel_type)
        except:
            raise ValueError(
                f"Please enter the valid Hotel Type. eg: {self.HotelType.THREE_STAR.value}, {self.HotelType.FIVE_STAR.value}, {self.HotelType.RESORT.value}"
            )

        try:
            self.Transport(self.transport)
        except:
            raise ValueError(
                f"Please enter the valid Transport. eg: {self.Transport.BUS.value}, {self.Transport.PRIVATE_CAB.value}, {self.Transport.NO_TRANSPORT.value}"
            )

        itinerary = TravelPackage(self)
        self.__init__()
        return itinerary


class TravelPackageDirector:
    def __init__(self, builder: TravelPackageBuilder) -> None:
        if not isinstance(builder, TravelPackageBuilder):
            raise ValueError("builder must be a TravelPackageBuilder instance.")

        self.builder = builder

    def honeymoon_package(self, destination: str) -> TravelPackage:
        return (
            self.builder.add_destination(destination)
            .add_flight_class("First Class")
            .add_hotel_type("Resort")
            .add_meal_plan("No Meals")
            .add_instruction("Honeymoon Trip")
            .build()
        )

    def family_package(self, destination: str) -> TravelPackage:
        return (
            self.builder.add_destination(destination)
            .add_flight_class("First Class")
            .add_hotel_type("5 Star")
            .add_meal_plan("Full Board")
            .add_transport("Private Cab")
            .add_instruction("Zoo Tour")
            .build()
        )


def main() -> None:
    honeymoon_pack = TravelPackageDirector(TravelPackageBuilder()).honeymoon_package(
        "Winland"
    )

    family_pack = TravelPackageDirector(TravelPackageBuilder()).family_package("India")
    print(honeymoon_pack.get_details())

    print(family_pack.get_details())

    custom = (
        TravelPackageBuilder()
        .add_destination("Japan")
        .add_flight_class("First Class")
        .add_hotel_type("Resort")
        .add_excursions("Watching Sakura")
        .add_excursions("See the Naruto Park")
        .add_instruction("I want to rent a girlfriend")
        .build()
    )

    print(custom.get_details())


if __name__ == "__main__":
    main()
