from pprint import pprint


class Product:
    def __init__(
        self,
        name: str = "",
        color: str = "#000",
        price: float = 0.00,
        brand: str = None,
        year: int = None,
    ) -> None:
        self.name = name
        self.color = color
        self.price = price
        self.brand = brand
        self.year = year

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.brand}, ₹{self.price})"


class Mouse(Product):
    def __init__(self, *args, **kwargs) -> None:
        self.is_wireless: bool = kwargs.pop("is_wireless", False)
        self.is_rgb: bool = kwargs.pop("is_rgb", False)
        super().__init__(*args, **kwargs)


class Speaker(Product):
    def __init__(self, *args, **kwargs) -> None:
        self.is_wireless: bool = kwargs.pop("is_wireless", False)
        super().__init__(*args, **kwargs)


class Keyboard(Product):
    def __init__(self, *args, **kwargs) -> None:
        self.is_wireless: bool = kwargs.pop("is_wireless", False)
        super().__init__(*args, **kwargs)


class Monitor(Product):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Processor(Product):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class Desktop:
    def __init__(self, builder) -> None:
        self.brand: str = builder.brand
        self.color: str = builder.color
        self.processor: Processor = builder.processor
        self.monitor: Monitor = builder.monitor
        self.keyboard: Keyboard = builder.keyboard
        self.mouse: Mouse = builder.mouse
        self.speakers: list[Speaker] = builder.speakers

    def get_details(self) -> dict:
        """
        To view all the details of the Desktop
        """

        return {
            "brand": self.brand,
            "color": self.color,
            "processor": vars(self.processor),
            "monitor": vars(self.monitor),
            "keyboard": vars(self.keyboard),
            "mouse": vars(self.mouse),
            "speakers": [vars(speaker) for speaker in self.speakers],
        }


class DesktopBuilder:
    def __init__(self) -> None:
        self.brand = None
        self.color = "#000"
        self.keyboard = None
        self.mouse = None
        self.processor = None
        self.speakers = []

    def set_brand(self, value: str):
        self.brand = value
        return self

    def set_color(self, color: str):
        self.color = color
        return self

    def set_keyboard(self, keyboard: Keyboard):
        if not isinstance(keyboard, Keyboard):
            raise ValueError("Keyboard must be a Keyboard instance.")
        self.keyboard = keyboard
        return self

    def set_mouse(self, mouse: Mouse):
        if not isinstance(mouse, Mouse):
            raise ValueError("mouse must be a Mouse instance.")
        self.mouse = mouse
        return self

    def set_speaker(self, speaker: Speaker):
        if not isinstance(speaker, Speaker):
            raise ValueError("speaker must be a Speaker instance.")

        self.speakers.append(speaker)
        return self

    def set_monitor(self, monitor: Monitor):
        if not isinstance(monitor, Monitor):
            raise ValueError("monitor must be a Monitor instance.")
        self.monitor = monitor
        return self

    def set_processor(self, processor: Processor):
        if not isinstance(processor, Processor):
            raise ValueError("processor must be a Processor instance.")

        self.processor = processor
        return self

    def build(self) -> Desktop:
        if not self.brand:
            raise ValueError("Please add the brand name")

        desktop = Desktop(self)
        self.__init__()
        return desktop


class DesktopDirector:
    def __init__(self, builder: DesktopBuilder) -> None:
        self.builder = builder

    def build_gaming_desktop(self) -> Desktop:
        return (
            self.builder.set_brand("Dell")
            .set_keyboard(Keyboard())
            .set_monitor(Monitor())
            .set_mouse(Mouse(is_rgb=True, is_wireless=True))
            .set_speaker(Speaker(is_wireless=True))
            .set_speaker(Speaker(is_wireless=True))
            .set_processor(Processor())
            .build()
        )


def main() -> None:
    gaming_desktop = DesktopDirector(DesktopBuilder()).build_gaming_desktop()
    pprint(gaming_desktop.get_details())


if __name__ == "__main__":
    main()
