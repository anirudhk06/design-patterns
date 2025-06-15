class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=SingletonMeta):
    def __init__(self) -> None:
        pass


def main() -> None:
    game1 = Game()
    game2 = Game()

    print(game1 is game2)


if __name__ == "__main__":
    main()
