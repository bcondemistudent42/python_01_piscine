from typing import Tuple


class Secure_Plant:
    """A plant model that exposes controlled getters and setters.

    The setters validate that numeric values are non-negative.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the secure plant.

        Args:
            name: Plant name.
            height: Height in centimeters.
            age: Age in days.
        """
        self.__name: str = name
        self.__height: int = height
        self.__age: int = age
        print(f"Created {self.__name} ({self.__height}, {self.__age})")

    def grow(self) -> None:
        """Simulate one week of growth (adds 7 cm)."""
        self.__height += 7
        print("Growth this week 7cm")

    def aging(self) -> None:
        """Simulate one week of aging (adds 7 days)."""
        self.__age += 7

    def get_info(self) -> None:
        """Print information about the plant."""
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def get_height(self) -> int:
        """Return the plant height in centimeters."""
        return (self.__height)

    def get_age(self) -> int:
        """Return the plant age in days."""
        return (self.__age)

    def set_height(self, value: int) -> None:
        """Set the plant height if the value is non-negative.

        Prints an error and returns early if value is negative.
        """
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__height = value
        print("Height updated", value, "[OK]")

    def set_age(self, value: int) -> None:
        """Set the plant age if the value is non-negative.

        Prints an error and returns early if value is negative.
        """
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__age = value
        print("Age updated", value, "[OK]")


class Factory:
    """Factory to create Secure_Plant instances from tuples."""

    def create_plant(my_data: Tuple[str, int, int]) -> Secure_Plant:
        """Create a Secure_Plant from a (name, height, age) tuple."""
        return (Secure_Plant(my_data[0], my_data[1], my_data[2]))


def main() -> None:
    flower: Secure_Plant = Secure_Plant("Rose", 25, 30)
    flower.get_info()
    flower.set_height(-421)
    flower.set_age(-21)
    flower.set_age(21)
    flower.set_height(42)
    print(flower.get_age())
    print(flower.get_height())
    flower.get_info()


if (__name__ == "__main__"):
    main()
