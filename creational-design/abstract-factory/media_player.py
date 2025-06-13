from abc import ABC, abstractmethod


class PlayButton(ABC):
    @abstractmethod
    def render() -> None:
        pass


class VolumeSlider(ABC):
    @abstractmethod
    def render() -> None:
        pass


class ScreenView(ABC):
    @abstractmethod
    def render() -> None:
        pass


class MobilePlayButton(PlayButton):
    @staticmethod
    def render() -> None:
        print("Rendering mobile play button with touch support")


class MobileVolumeSlider(VolumeSlider):
    @staticmethod
    def render() -> None:
        print("Rendering mobile volume slider with swipe gesture")


class MobileScreenView(ScreenView):
    @staticmethod
    def render() -> None:
        print("Rendering mobile screen view with pinch-to-zoom")


class DesktopPlayButton(PlayButton):
    @staticmethod
    def render() -> None:
        print("Rendering desktop play button with mouse support")


class DesktopVolumeSlider(VolumeSlider):
    @staticmethod
    def render() -> None:
        print("Rendering desktop volume slider with click and drag")


class DesktopScreenView(ScreenView):
    @staticmethod
    def render() -> None:
        print("Rendering desktop screen view with window resize support")


class UIFactory:
    @abstractmethod
    def create_play_button() -> PlayButton: ...
    @abstractmethod
    def create_volume_slider() -> VolumeSlider: ...
    @abstractmethod
    def create_screen_view() -> ScreenView: ...


class MobileUIFactory(UIFactory):
    def __init__(self) -> None:
        print("Platform: Mobile")

    @staticmethod
    def create_play_button() -> MobilePlayButton:
        return MobilePlayButton()

    @staticmethod
    def create_volume_slider() -> MobileVolumeSlider:
        return MobileVolumeSlider()

    @staticmethod
    def create_screen_view() -> MobileScreenView:
        return MobileScreenView()


class DesktopUIFactory(UIFactory):
    def __init__(self) -> None:
        print("Platform: Desktop")

    @staticmethod
    def create_play_button() -> DesktopPlayButton:
        return DesktopPlayButton()

    @staticmethod
    def create_volume_slider() -> DesktopVolumeSlider:
        return DesktopVolumeSlider()

    @staticmethod
    def create_screen_view() -> DesktopScreenView:
        return DesktopScreenView()


def main() -> None:

    platform = input("Chose platform (mobile/desktop): ").lower().strip()

    factory: UIFactory = None
    match platform:
        case "mobile":
            factory = MobileUIFactory()
        case "desktop":
            factory = DesktopUIFactory()
        case _:
            raise ValueError("Invalid input. Available platforms are 'mobile/desktop'")

    button = factory.create_play_button()
    volume_slider = factory.create_volume_slider()
    screen_view = factory.create_screen_view()
    button.render()
    volume_slider.render()
    screen_view.render()


if __name__ == "__main__":
    main()
