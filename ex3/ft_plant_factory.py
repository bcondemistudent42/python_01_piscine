
class Plant:
    def __init__(self, name: str, height: int, age: int):
        """A class for the creation of Plant, with 3 parameters"""
        self.name = name
        self.height = height
        self.age = age
        print(f"Created {self.name} ({self.height}, {self.age})")

    def grow(self):
        """A method that increase the size of plant by seven because
        its a week simulation and we admit that it grows 1cm a day and print
        the size of how many cm it grows"""
        self.height += 7
        print("Growth this week 7cm")

    def aging(self):
        """A method that increase the age of plant by one week"""
        self.age += 7

    def get_info(self):
        """A method that let u know the status of the plant"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Factory():
    """A factory class to create a function create plant"""
    def create_plant(my_data):
        """A create plant function to make a lot of plant"""
        return (Plant(my_data[0], my_data[1], my_data[2]))


if (__name__ == "__main__"):
    data = [
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
