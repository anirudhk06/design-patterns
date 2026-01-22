from abc import ABC, abstractmethod


class WeatherServiceInterface(ABC):
    @abstractmethod
    def get_weather(self, city: str) -> str:
        pass


class WeatherService(WeatherServiceInterface):
    def get_weather(self, city: str) -> str:
        print(f"[API CALL] Fetching weather for {city}")
        return f"Weather data for {city}"


class WeatherServiceProxy(WeatherServiceInterface):
    def __init__(self):
        self._service = WeatherService()
        self._cache: dict[str, str] = {}

    def get_weather(self, city):
        key = city.strip().lower()

        if key in self._cache:
            return self._cache[key]

        data = self._service.get_weather(city)
        self._cache[key] = data
        return data


def main() -> None:
    service = WeatherServiceProxy()

    print(service.get_weather("London"))
    print(service.get_weather("London"))
    print(service.get_weather("Paris"))


if __name__ == "__main__":
    main()
