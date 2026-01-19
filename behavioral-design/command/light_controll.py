from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError("Sub classes must be implement execute() method.")

    @abstractmethod
    def undo(self):
        raise NotImplementedError("Sub classes must be implement undo() method.")


class LightOnCommand(Command):
    def __init__(self, light: "Light"):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: "Light"):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


class RemoteController:
    def __init__(self):
        self.history: list[Command] = []

    def press(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if not self.history:
            return

        last_command = self.history.pop()
        last_command.undo()


def main() -> None:
    light = Light()
    remote = RemoteController()
    light_on = LightOnCommand(light)

    remote.press(light_on)

    remote.undo()
    remote.undo()


if __name__ == "__main__":
    main()
