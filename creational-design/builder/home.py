from typing import Optional


class Home:
    def __init__(self, builder) -> None:
        self.rooms = builder.rooms
        self.doors = builder.doors
        self.windows = builder.windows
        self.roof_type = builder.roof_type
        self.floor = builder.floor


class HomeBuilder:
    def __init__(self) -> None:
        self.rooms: Optional[int] = None
        self.doors: Optional[int] = None
        self.windows: Optional[int] = None
        self.roof_type: Optional[int] = None
        self.floor: Optional[int] = None

    def build_rooms(self, value: int):
        self.rooms = value
        return self

    def build_doors(self, value: int):
        self.doors = value
        return self

    def build_windows(self, value: int):
        self.windows = value
        return self

    def build_roof_type(self, value: str):
        self.roof_type = value
        return self

    def build_floor(self, value: str):
        self.floor = value
        return self

    def build(self) -> Home:
        home = Home(self)
        self.__init__()
        return home


class Director:
    def __init__(self, builder: HomeBuilder) -> None:
        self.builder = builder

    def one_story(self) -> Home:
        return (
            self.builder.build_doors(2)
            .build_floor(1)
            .build_roof_type("pointer")
            .build()
        )

    def tow_story(self) -> Home:
        return self.builder.build_floor(2).build_roof_type("flat").build()


def main() -> None:
    home_builder = HomeBuilder()
    director = Director(home_builder)
    one_story = director.one_story()
    two_story = director.tow_story()

    print(one_story.doors)
    print(two_story.doors)


if __name__ == "__main__":
    main()
