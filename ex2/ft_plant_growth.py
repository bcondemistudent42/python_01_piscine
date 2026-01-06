
class Plant:
    def __init__(self, name, height, age):
        """A class for the creation of Plant, with 3 parameters"""
        self.name = name
        self.height = height
        self.age = age

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


if (__name__ == "__main__"):
    flower = Plant("Rose", 25, 30)
    flower.get_info()
    flower.grow()
    flower.aging()
    flower.get_info()
    flower1 = Plant("Sunflower", 85, 21)
    print("-----------------------")
    flower1.get_info()
    flower1.grow()
    flower1.aging()
    flower1.get_info()
