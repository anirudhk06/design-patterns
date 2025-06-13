from abc import ABC, abstractmethod
import copy


class Shape(ABC):
    @abstractmethod
    def clone(self) -> "Shape":
        pass


class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int, style: dict) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.style = style

    def __repr__(self) -> str:
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height}, style={self.style})"

    def clone(self) -> Shape:
        return copy.deepcopy(self)


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, style: dict[str, str]) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.style = style

    def __repr__(self) -> str:
        return (
            f"Circle(x={self.x}, y={self.y}, radius={self.radius}, style={self.style})"
        )

    def clone(self) -> Shape:
        return copy.deepcopy(self)


def main() -> None:
    rect = Rectangle(10, 10, 20, 20, {"color": "red"})
    rect_clone = rect.clone()

    print(rect)
    print(rect_clone)

    circle = Circle(10, 10, 200, {"color": "black"})
    circle_clone = circle.clone()

    print(circle)
    print(circle_clone)


if __name__ == "__main__":
    main()
