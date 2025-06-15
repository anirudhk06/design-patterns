from typing import Any
from types import MappingProxyType
import threading


class SingletonMeta(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, config=None) -> Any:

        if cls._instance is None:
            with cls._lock:
                cls._instance = super().__call__(config)

        else:
            if config is not None and cls._instance.config != config:
                raise ValueError(
                    "SettingsLoader already initialized with a different config."
                )
        return cls._instance


class SettingsLoader(metaclass=SingletonMeta):
    def __init__(self, config: dict = None) -> None:
        self._original_config = config or {}
        self.config = MappingProxyType(self._original_config)

    def get(self, key: str) -> Any | None:
        return self.config.get(key)


def main() -> None:
    config_data = {"debug": True, "db_host": "localhost", "port": 5432}
    settings1 = SettingsLoader(config_data)

    print(settings1.get("db_host"))

    settings2 = SettingsLoader(config_data)
    print(settings2.get("debug"))

    try:
        settings1.config["port"] = 8000
    except TypeError as e:
        print("Modification error:", e)

    try:
        SettingsLoader({"debug": False})
    except ValueError as e:
        print("Reinitialization error:", e)


if __name__ == "__main__":
    main()
