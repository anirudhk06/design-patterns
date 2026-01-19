from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, receiver: "Receiver"):
        raise NotImplementedError("Sub classes must be implement execute() method.")


class LightOnCommand(Command):
    def __init__(self, light: "Receiver"):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light: "Receiver"):
        self.light = light

    def execute(self):
        self.light.off()


class FanOnCommand(Command):
    def __init__(self, fan: "Receiver"):
        self.fan = fan

    def execute(self):
        self.fan.on()


class FanOffCommand(Command):
    def __init__(self, fan: "Receiver"):
        self.fan = fan

    def execute(self):
        self.fan.off()


class Receiver(ABC):
    @abstractmethod
    def on(self):
        raise NotImplementedError("Sub classes must be implement on() method.")

    @abstractmethod
    def off(self):
        raise NotImplementedError("Sub classes must be implement off() method.")


class Light(Receiver):
    def on(self):
        print("Light id on")

    def off(self):
        print("Light is off")


class Fan(Receiver):
    def on(self):
        print("Fan is on")

    def off(self):
        print("Fan is off")


class RemoteController:
    def press(self, command: Command):
        command.execute()


def main() -> None:
    light = Light()
    fan = Fan()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    fan_on = FanOnCommand(fan)
    fan_off = FanOffCommand(fan)

    remote = RemoteController()
    
    remote.press(light_on)
    remote.press(light_off)

    remote.press(fan_on)
    remote.press(fan_off)


if __name__ == "__main__":
    main()
