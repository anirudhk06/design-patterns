from typing import Any
import threading


class SingletonManager(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, config=None) -> Any:
        if cls._instance is None:
            with cls._lock:
                cls._instance = super().__call__(config)

        if config is not None and cls._instance.config != config:
            raise ValueError(
                "ConfigManager is already initialized with a different configuration."
            )
        return cls._instance


class ConfigManager(metaclass=SingletonManager):
    def __init__(self, config: dict = None) -> None:

        self.config = config

    def get(self, key: str) -> Any | None:
        return self.config.get(key)

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value


def main() -> None:
    config1 = ConfigManager({"debug": True, "db": "localhost"})
    config2 = ConfigManager({"debug": True, "db": "localhost"})

    print(config1.get("debug"))
    config2.set("debug", False)
    print(config1.get("debug"))

    print(config1 is config2)


if __name__ == "__main__":
    main()
