from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class LightButton(Button):
    def render(self) -> None:
        print("Rendering light button")


class DarkButton(Button):
    def render(self) -> None:
        print("Rendering dark button")


class LightCheckbox(Checkbox):
    def render(self) -> None:
        print("Rendering light checkbox")


class DarkCheckbox(Checkbox):
    def render(self) -> None:
        print("Rendering dark checkbox")


class UIFactory:
    @staticmethod
    def create_button() -> Button: ...
    @staticmethod
    def create_checkbox() -> Checkbox: ...


class LightThemeFactory(UIFactory):
    def __init__(self) -> None:
        print("Using light theme")

    def create_button(self) -> LightButton:
        return LightButton()

    def create_checkbox(self) -> LightCheckbox:
        return LightCheckbox()


class DarkThemeFactory(UIFactory):
    def __init__(self) -> None:
        print("Using dark theme")

    def create_button(self) -> DarkButton:
        return DarkButton()

    def create_checkbox(self) -> DarkCheckbox:
        return DarkCheckbox()


def main() -> None:
    light_theme = LightThemeFactory()
    light_button = light_theme.create_button()
    light_checkbox = light_theme.create_checkbox()
    light_button.render()
    light_checkbox.render()

    dark_theme = DarkThemeFactory()
    dark_button = dark_theme.create_button()
    dark_checkbox = dark_theme.create_checkbox()
    dark_button.render()
    dark_checkbox.render()


if __name__ == "__main__":
    main()
