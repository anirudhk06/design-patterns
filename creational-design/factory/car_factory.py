from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        raise NotImplementedError("subclasses must be implement start() method")

    @abstractmethod
    def stop(self):
        raise NotImplementedError("subclasses must be implement stop() method")


class Car(Vehicle):
    def start(self):
        print("Car is started")

    def stop(self):
        print("Car is stopped")


class Truck(Vehicle):
    def start(self):
        print("Truck is started")

    def stop(self):
        print("Truck is stopped")


class VehicleFactory:
    def get_vehicle(self, vehicle_type: str) -> Vehicle:
        match vehicle_type:
            case "car":
                return Car()
            case "truck":
                return Truck()

        raise Exception("Invalid vehicle_type")


def main() -> None:
    car1 = VehicleFactory.get_vehicle("car")
    car2 = VehicleFactory.get_vehicle("car")
    truck1 = VehicleFactory.get_vehicle("truck")
    truck2 = VehicleFactory.get_vehicle("truck")


if __name__ == "__main__":
    main()
