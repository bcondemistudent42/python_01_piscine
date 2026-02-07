from typing import Tuple


class Base_Plant:
    """Base plant providing common attributes and simple validation.

    Attributes:
        __name: str - plant name (private)
        __height: int - height in cm (private)
        __age: int - age in days (private)
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name: str = name
        self.__height: int = height
        self.__age: int = age
        print(f"Created {self.__name} ({self.__height}, {self.__age})")

    def grow(self) -> None:
        """Simulate weekly growth (adds 7 cm)."""
        self.__height += 7
        print("Growth this week 7cm")

    def aging(self) -> None:
        """Simulate weekly aging (adds 7 days)."""
        self.__age += 7

    def get_info(self) -> None:
        """Print the plant's information."""
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def get_height(self) -> int:
        """Return height in centimeters."""
        return (self.__height)

    def get_age(self) -> int:
        """Return age in days."""
        return (self.__age)

    def get_name(self) -> str:
        """Return the plant's name."""
        return (self.__name)

    def set_height(self, value: int) -> None:
        """Set height to value if non-negative; otherwise print an error."""
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__height = value
        print("Height updated", value, "[OK]")

    def set_age(self, value: int) -> None:
        """Set age to value if non-negative; otherwise print an error."""
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__age = value
        print("Age updated", value, "[OK]")


class Flower(Base_Plant):
    """Flower type with color and bloom behavior."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.__color: str = color

    def get_info(self) -> None:
        """Print information including the flower color."""
        n: str = self.get_name()
        h: int = self.get_height()
        a: int = self.get_age()
        print(f"{n} (Flower): {h} cm, {a} days, {self.get_color()}")

    def bloom(self) -> None:
        """Announce that the flower is blooming."""
        print(f"{self.get_name()} is blooming beautifully !")

    def get_color(self) -> str:
        """Return the flower's color."""
        return (self.__color)


class Tree(Base_Plant):
    """Tree type with trunk diameter and shade calculation."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.__trunk_diameter: int = trunk_diameter

    def get_info(self) -> None:
        """Print info including trunk diameter."""
        n: str = self.get_name()
        h: int = self.get_height()
        a: int = self.get_age()
        d: str = "cm diameter"
        print(f"{n} (Tree): {h} cm, {a} days, {self.get_diameter()} {d}")

    def get_diameter(self) -> int:
        """Return trunk diameter in cm."""
        return (self.__trunk_diameter)

    def produce_shade(self) -> None:
        """Estimate and print square meters of shade produced."""
        res: float = (int(self.get_diameter()) * 1.56)
        print(f"{self.get_name()} provides {int(res)} square meters of shade ")


class Vegetable(Base_Plant):
    """Vegetable type with harvest season and nutritional info."""

    def __init__(self, nam: str, heit: int, age: int, harv: str, nut: str):
        super().__init__(nam, heit, age)
        self.__harvest_season: str = harv
        self.__nutritional_value: str = nut

    def get_info(self) -> None:
        """Print info and nutritional information for the vegetable."""
        name: str = self.get_name()
        height: int = self.get_height()
        age: int = self.get_age()
        print(f"{name} (Vegetables): {height} cm, {age} days, {self.get_hr()}")
        print(f"{name} is rich in {self.get_nutritional_value()}")

    def get_nutritional_value(self) -> str:
        """Return a short description of nutritional value."""
        return (self.__nutritional_value)

    def get_hr(self) -> str:
        """Return the harvest season string."""
        return (self.__harvest_season)


class Factory:
    """Factory returning a Base_Plant for simple tuple data."""

    def create_plant(my_data: Tuple[str, int, int]) -> Base_Plant:
        """Create a Base_Plant from a tuple (name, height, age)."""
        return (Base_Plant(my_data[0], my_data[1], my_data[2]))


def main() -> None:
    flower: Flower = Flower("Rose", 25, 30, "red")
    flower.bloom()
    flower1: Flower = Flower("Viola", 41, 42, "purple")
    flower1.bloom()
    print(flower.get_color())
    print(flower1.get_color())
    flower.get_info()
    flower1.get_info()
    print("=================================")
    tree: Tree = Tree("Oak", 500, 1825, 50)
    tree1: Tree = Tree("Pin", 900, 2000, 95)
    tree.get_info()
    tree.produce_shade()
    tree1.get_info()
    tree1.produce_shade()
    print("=================================")
    vege = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    vege1 = Vegetable("Salad", 10, 15, "winter harvest", "vitamin B")
    vege.get_info()
    vege1.get_info()


if (__name__ == "__main__"):
    main()
