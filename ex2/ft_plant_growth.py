class Plant:
    """Represents a plant with a name, height, and age.

    Methods are provided to simulate weekly growth and aging and to
    print the plant's information.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        :param name: The name of the plant.
        :param height: The height of the plant in centimeters.
        :param age: The age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        """
        Simulate one week of growth.

        The plant grows 1 cm per day, resulting in a total growth
        of 7 cm over one week.
        """
        self.height += 7
        print("Growth this week: 7 cm")

    def aging(self) -> None:
        """
        Simulate one week of aging.

        Increases the plant's age by 7 days.
        """
        self.age += 7

    def get_info(self) -> None:
        """
        Display the current state of the plant.

        Shows the name, height (in cm), and age (in days).
        """
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def main() -> None:
    """
    Main function used to test the Plant class.
    """
    flower: Plant = Plant("Rose", 25, 30)
    flower.get_info()
    flower.grow()
    flower.aging()
    flower.get_info()

    flower1: Plant = Plant("Sunflower", 85, 21)
    print("-----------------------")
    flower1.get_info()
    flower1.grow()
    flower1.aging()
    flower1.get_info()


if __name__ == "__main__":
    main()
