
class Plant:
    def __init__(self, name, height, age):
        """A class for the creation of Plant, with 3 parameters"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """A method that increase the size of plant by one"""
        self.height = self.height + 1

    def age(self):
        """A method that increase the age of plant by one day"""
        self.age = self.age + 1

    def get_info(self):
        """A method that let u know the status of the plant"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")
