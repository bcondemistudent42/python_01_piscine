from typing import Tuple


class Secure_Plant:
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


class Factory:
    def create_plant(my_data: Tuple[str, int, int]) -> Secure_Plant:
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
