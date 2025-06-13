from abc import ABC, abstractmethod
import copy


class ProfilePrototype(ABC):
    @abstractmethod
    def clone(self) -> "ProfilePrototype":
        pass


class UserProfile(ProfilePrototype):
    def __init__(self, name: str, age: int, preferences: dict[str, str]) -> None:
        self.name = name
        self.age = age
        self.preferences = preferences

    def set_preferences(self, key: str, value: str) -> None:
        self.preferences[key] = value

    def clone(self) -> "UserProfile":
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: name={self.name}, age={self.age}, preferences={self.preferences}>"


def main() -> None:
    user = UserProfile("Anirudh k", 24, {"theme": "dark"})
    clone = user.clone()
    clone.set_preferences("theme", "light")

    print("Original: ", user)
    print("Clone: ", clone)


if __name__ == "__main__":
    main()
