
class Plant:
    def __init__(self, name, height, age):
        """A class for the creation of Plant, with 3 parameters"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """A method that increase the size of plant by one"""
        self.height += 1

    def aging(self):
        """A method that increase the age of plant by one day"""
        self.age += 1

    def get_info(self):
        """A method that let u know the status of the plant"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if (__name__ == "__main__"):
    flower = Plant("Rose", 25, 30)
    flower.get_info()
    # flower.grow()
    # flower.aging()
    flower.get_info()
    i = 0
    while (i < 7):
        flower.grow()
        flower.aging()
        i += 1
    print("-----After the while loop-----")
    flower.get_info()
