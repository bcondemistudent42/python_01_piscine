
class Plant:
    def __init__(self, name, height, age):
        """A class for the creation of Plant, with 3 parameters"""
        self.name = name
        self.height = height
        self.age = age


if (__name__ == "__main__"):
    flower = Plant("Rose", 25, 30)
    flower1 = Plant("Sunflower", 80, 45)
    flower2 = Plant("Cactus", 15, 120)
    print(f"{flower.name}: {flower.height}cm, {flower.age} days old")
    print(f"{flower1.name}: {flower1.height}cm, {flower1.age} days old")
    print(f"{flower2.name}: {flower2.height}cm, {flower2.age} days old")
