from abc import ABC, abstractmethod
import copy


class GameCharacterPrototype(ABC):
    @abstractmethod
    def clone(self) -> "GameCharacterPrototype":
        pass


class GameCharacter(GameCharacterPrototype):
    def __init__(
        self,
        name: str,
        level: int = 1,
        stats: dict[str, int] = {},
        gear: dict[str, str] = {},
        skills: dict[str, dict[str, int]] = {},
    ) -> None:
        self.name = name
        self.level = level
        self.stats = stats
        self.gear = gear
        self.skills = skills

    def level_up(self) -> None:
        self.level += 1

        for key in self.stats:
            self.stats[key] += 1

    def update_skill(self, category: str, skill: str, points: int) -> None:
        if category not in self.skills:
            self.skills[category] = {}

        self.skills[category][skill] = self.skills[category].get(skill, 0) + points

    def equip_item(self, slot: str, item: str) -> None:
        self.gear[slot] = item

    def clone(self) -> GameCharacterPrototype:
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return (
            f"<{self.name} | Lv:{self.level} | "
            f"Stats:{self.stats} | Gear:{self.gear} | Skills:{self.skills}>"
        )


def main() -> None:
    warrior = GameCharacter(
        name="Warrior",
        level=10,
        stats={"strength": 15, "agility": 10, "intelligence": 5},
        gear={"weapon": "Iron Sword", "armor": "Leather Armor"},
        skills={"offense": {"slash": 2}, "defense": {"block": 3}},
    )

    clone_warrior = warrior.clone()
    clone_warrior.update_skill("offense", "frenzy", 3)
    clone_warrior.equip_item("weapon", "Flaming Sword")
    clone_warrior.level_up()

    print("Original:", warrior)
    print("Clone:   ", clone_warrior)


if __name__ == "__main__":
    main()
