from typing import Tuple


class BasePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name: str = name
        self.__height: int = height
        self.__age: int = age
        print(f"Created {self.__name} ({self.__height}, {self.__age})")

    def grow(self) -> None:
        self.__height += 7
        print("Growth this week 7cm")

    def aging(self) -> None:
        self.__age += 7

    def get_info(self) -> None:
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def get_height(self) -> int:
        return (self.__height)

    def get_age(self) -> int:
        return (self.__age)

    def get_name(self) -> str:
        return (self.__name)

    def get_type(self) -> str:
        return "Base_Plant"

    def set_height(self, value: int) -> None:
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__height = value
        print("Height updated", value, "[OK]")

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__age = value
        print("Age updated", value, "[OK]")


class Garden:
    def __init__(self, name: str):
        self.__name = name
        self.__lst_plant = []
        self.__lst_flowering = []
        self.__lst_prize = []

    def add_plant(self, plant: BasePlant) -> None:
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

    def get_name(self) -> None:
        return (self.__name)

    def get_plant(self):
        return (self.__lst_plant)


class GardenManager:
    class GardenStats:
        def __init__(self, lst: list):
            self.lst = lst

        def get_len(self):
            print(len(self.lst))

        def get_flower(self, index: int):
            print(len(self.lst[index].get_plant()))

    def __init__(self):
        self.__lst = []
        self.stats = self.GardenStats(self.__lst)

    def add_garden(self, garden: Garden):
        self.__lst.append(garden)

    def get_index(self):
        i: int = 0
        for elt in self.__lst:
            print(f"Garden == {elt.get_name()}, i == {i}")
            i += 1

    # def create_garden_network(cls) -> 'Garden_Manager':
    #     return cls()


class FloweringPlant(BasePlant):
    def __init__(self, name: str, height: int, age: int):
        super().__init__(name, height, age)

    def get_type(self) -> str:
        return "Flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int):
        super().__init__(name, height, age)

    def get_type(self) -> str:
        return "Prize"


class Flower(BasePlant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.__color: str = color

    def get_info(self) -> None:
        n: str = self.get_name()
        h: int = self.get_height()
        a: int = self.get_age()
        print(f"{n} (Flower): {h} cm, {a} days, {self.get_color()}")

    def bloom(self) -> None:
        print(f"{self.get_name()} is blooming beautifully !")

    def get_color(self) -> str:
        return (self.__color)


class Tree(BasePlant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.__trunk_diameter: int = trunk_diameter

    def get_info(self) -> None:
        n: str = self.get_name()
        h: int = self.get_height()
        a: int = self.get_age()
        d: str = "cm diameter"
        print(f"{n} (Tree): {h} cm, {a} days, {self.get_diameter()} {d}")

    def get_diameter(self) -> int:
        return (self.__trunk_diameter)

    def produce_shade(self) -> None:
        res: float = (int(self.get_diameter()) * 1.56)
        print(f"{self.get_name()} provides {int(res)} square meters of shade ")


class Vegetable(BasePlant):
    def __init__(self, nam: str, heit: int, age: int, harv: str, nut: str):
        super().__init__(nam, heit, age)
        self.__harvest_season: str = harv
        self.__nutritional_value: str = nut

    def get_info(self) -> None:
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
        return (BasePlant(my_data[0], my_data[1], my_data[2]))


def main() -> None:
    manager = GardenManager()
    garden = Garden("Alice")
    garden1 = Garden("Robert")
    manager.add_garden(garden)
    manager.add_garden(garden1)
    plant = FloweringPlant("Rose", 25, 2)
    plant1 = BasePlant("Violete", 12, 7)
    plant2 = PrizeFlower("Sunflower", 21, 12)
    garden.add_plant(plant)
    garden.add_plant(plant1)
    garden.add_plant(plant2)
    garden1.add_plant(plant)
    garden1.add_plant(plant1)
    garden1.add_plant(plant2)
    # garden.get_name()
    manager.get_index()
    # manager.stats.get_flower(0)


if (__name__ == "__main__"):
    main()
