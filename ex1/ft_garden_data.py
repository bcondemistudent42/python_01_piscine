class Plant:
    """Represents a plant with a name, height, and age.

    Attributes:
        name: The plant's name.
        height: Height in centimeters.
        age: Age in days.
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


def main() -> None:
    """
    Main function used to create Plant objects and display their information.
    """
    flower: Plant = Plant("Rose", 25, 30)
    flower1: Plant = Plant("Sunflower", 80, 45)
    flower2: Plant = Plant("Cactus", 15, 120)

    print(f"{flower.name}: {flower.height} cm, {flower.age} days old")
    print(f"{flower1.name}: {flower1.height} cm, {flower1.age} days old")
    print(f"{flower2.name}: {flower2.height} cm, {flower2.age} days old")


if __name__ == "__main__":
    main()
