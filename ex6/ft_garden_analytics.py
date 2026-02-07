from typing import Tuple, List


class BasePlant:
    """Core plant class used by the garden analytics tools.

    Contains minimal state and basic operations like grow and aging.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
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
        """Print the current state of the plant."""
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

    def get_type(self) -> str:
        """Return a short type identifier for this plant class."""
        return "Base_Plant"

    def set_height(self, value: int) -> None:
        """Set height if non-negative, otherwise print an error."""
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__height = value
        print("Height updated", value, "[OK]")

    def set_age(self, value: int) -> None:
        """Set age if non-negative, otherwise print an error."""
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__age = value
        print("Age updated", value, "[OK]")


class FloweringPlant(BasePlant):
    """Marker subclass for flowering plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

    def get_type(self) -> str:
        """Return the type identifier for flowering plants."""
        return "Flowering"


class PrizeFlower(FloweringPlant):
    """Special flowering plant type representing prize flowers."""

    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

    def get_type(self) -> str:
        """Return the short type identifier for prize flowers."""
        return "Prize"


class Garden:
    """Container for plants with simple categorization lists.
    Stores lists for all plants, flowering plants and prize flowers.
    """

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__lst_plant: list[BasePlant] = []
        self.__lst_flowering: list[BasePlant] = []
        self.__lst_prize: list[BasePlant] = []

    def add_plant(
        self, plant: BasePlant | PrizeFlower | FloweringPlant
    ) -> None:
        """Add a plant to appropriate internal lists based on its type."""
        if (plant.get_type() == "Prize"):
            self.__lst_plant.append(plant)
            self.__lst_flowering.append(plant)
            self.__lst_prize.append(plant)
            return
        if (plant.get_type() == "Flowering"):
            self.__lst_plant.append(plant)
            self.__lst_flowering.append(plant)
            return
        self.__lst_plant.append(plant)

    def get_name(self) -> str:
        """Return the garden name."""
        return (self.__name)

    def get_plant(self) -> List[BasePlant]:
        """Return list of all plants in the garden."""
        return (self.__lst_plant)

    def get_flowering(self) -> List[BasePlant]:
        """Return list of flowering plants in the garden."""
        return (self.__lst_flowering)

    def get_prize(self) -> List[BasePlant]:
        """Return list of prize flowers in the garden."""
        return (self.__lst_prize)


class GardenManager:
    """Manager for multiple gardens and basic aggregate operations."""

    class GardenStats:
        """Utility class that prints simple statistics about gardens."""

        def __init__(self, lst: list) -> None:
            self.lst = lst

        def get_len(self) -> None:
            """Print number of gardens tracked."""
            print(len(self.lst))

        def get_plant_nbr(self, index: int) -> None:
            """Print number of plants in the garden at index."""
            print(f"There is {len(self.lst[index].get_plant())} Plants")

        def get_flowering_nbr(self, index: int) -> None:
            """Print number of flowering plants in the garden at index."""
            print(f"{len(self.lst[index].get_flowering())} are Flowering")

        def get_prize_nbr(self, index: int) -> None:
            """Print number of prize flowers in the garden at index."""
            print(f"There is {len(self.lst[index].get_prize())} Prize Flower")

        def grow_all(self, index: int) -> None:
            """Grow every plant in the garden at index and print total.

            This method calls each plant's grow() method and prints the
            cumulative growth produced (assuming 7 cm per plant per
            grow() call used in these exercises).
            """
            print(f"{self.lst[index].get_name()} helps all plant to grow")
            i: int = 0
            for elt in self.lst[index].get_plant():
                elt.grow()
                i += 1
            print(f"Total growth = {7 * i}cm")

    def __init__(self) -> None:
        self.__lst: List[Garden] = []
        self.stats = self.GardenStats(self.__lst)

    def add_garden(self, garden: Garden) -> None:
        """Append a Garden instance to the manager."""
        self.__lst.append(garden)

    def get_index(self) -> None:
        """Print index and name for each garden tracked."""
        i: int = 0
        for elt in self.__lst:
            print(f"Garden == {elt.get_name()}, i == {i}")
            i += 1

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        """Create and return a GardenManager instance.

        The first parameter is named `cls` to allow use as a factory
        style method; calling `GardenManager.create_garden_network()`
        constructs and returns a new manager instance.
        """
        instance: 'GardenManager' = cls()
        return instance


class Flower(BasePlant):
    """Flower subclass providing color and bloom behavior."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.__color: str = color

    def get_info(self) -> None:
        n: str = self.get_name()
        h: int = self.get_height()
        a: int = self.get_age()
        print(f"{n} (Flower): {h} cm, {a} days, {self.get_color()}")

    def bloom(self) -> None:
        """Simulate the flower blooming (prints a short message)."""
        print(f"{self.get_name()} is blooming beautifully !")

    def get_color(self) -> str:
        """Return the flower color as a string."""
        return (self.__color)


class Tree(BasePlant):
    """Tree subclass that exposes trunk diameter and shade metrics."""

    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        """Initialize a Tree instance.

        Args:
            name: Human-readable name for the tree.
            height: Height in centimeters.
            age: Age in days.
            trunk_diameter: Diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.__trunk_diameter: int = trunk_diameter

    def get_info(self) -> None:
        n: str = self.get_name()
        h: int = self.get_height()
        a: int = self.get_age()
        d: str = "cm diameter"
        print(f"{n} (Tree): {h} cm, {a} days, {self.get_diameter()} {d}")

    def get_diameter(self) -> int:
        """Return the trunk diameter in centimeters."""
        return (self.__trunk_diameter)

    def produce_shade(self) -> None:
        """Estimate and print the square meters of shade produced.

        The algorithm uses a simple multiplier on trunk diameter to
        approximate shade area; this is a toy example for exercises.
        """
        res: float = (int(self.get_diameter()) * 1.56)
        print(f"{self.get_name()} provides {int(res)} square meters of shade ")


class Vegetable(BasePlant):
    def __init__(
        self, nam: str, heit: int, age: int, harv: str, nut: str
    ) -> None:
        """Initialize a Vegetable instance.

        Args:
            nam: Name of the vegetable.
            heit: Height in centimeters.
            age: Age in days.
            harv: Harvest season description.
            nut: Short description of nutritional value.
        """
        super().__init__(nam, heit, age)
        self.__harvest_season: str = harv
        self.__nutritional_value: str = nut

    def get_info(self) -> None:
        """Print a multi-line info summary for this vegetable."""
        name: str = self.get_name()
        height: int = self.get_height()
        age: int = self.get_age()
        print(f"{name} (Vegetables): {height} cm, {age} days, {self.get_hr()}")
        print(f"{name} is rich in {self.get_nutritional_value()}")

    def get_nutritional_value(self) -> str:
        return (self.__nutritional_value)

    def get_hr(self) -> str:
        return (self.__harvest_season)


class Factory:
    def create_plant(my_data: Tuple[str, int, int]) -> BasePlant:
        """Create and return a BasePlant from a (name, height, age)
        tuple.

        Args:
            my_data: A tuple containing (name, height_cm, age_days).

        Returns:
            A new BasePlant instance constructed from the tuple.
        """
        return (BasePlant(my_data[0], my_data[1], my_data[2]))


def main() -> None:
    manager = GardenManager.create_garden_network()
    garden = Garden("Alice")
    garden1 = Garden("Robert")
    manager.add_garden(garden)
    manager.add_garden(garden1)
    plant = FloweringPlant("Rose", 25, 2)
    plant1 = BasePlant("Violete", 12, 7)
    plant2 = PrizeFlower("Sunflower", 21, 12)
    plant3 = BasePlant("White", 10, 10)
    garden.add_plant(plant)
    garden.add_plant(plant1)
    garden.add_plant(plant2)
    garden1.add_plant(plant)
    garden1.add_plant(plant1)
    garden1.add_plant(plant2)
    garden1.add_plant(plant3)
    garden.get_name()
    manager.get_index()
    manager.stats.grow_all(1)


if (__name__ == "__main__"):
    main()
