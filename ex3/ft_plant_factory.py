from typing import List, Tuple


class Plant:
    """A lightweight Plant model used by the factory.

    Attributes:
        name: Plant name.
        height: Height in centimeters.
        age: Age in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        print(f"Created {self.name} ({self.height}, {self.age})")

    def grow(self) -> None:
        """Simulate one week of growth (adds 7 cm)."""
        self.height += 7
        print("Growth this week 7cm")

    def aging(self) -> None:
        """Simulate one week of aging (adds 7 days)."""
        self.age += 7

    def get_info(self) -> None:
        """Print human-readable info for the plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Factory:
    """Simple factory which creates Plant objects from a tuple.

    The create_plant function expects a tuple (name, height, age) and
    returns a new Plant instance.
    """

    def create_plant(my_data: Tuple[str, int, int]) -> Plant:
        """Create a Plant from a (name, height, age) tuple.

        Args:
            my_data: Tuple[str, int, int] containing name, height, age.

        Returns:
            Plant: the created Plant instance.
        """
        return (Plant(my_data[0], my_data[1], my_data[2]))


def main() -> None:
    data: List[Tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
            ]
    i: int = 0
    while (i < 5):
        Factory.create_plant(data[i])
        i += 1
    print("Total plants created: 5")


if (__name__ == "__main__"):
    main()
