
class Plant:
    def __init__(self, name, height, age):
        """A class for the creation of Plant, with 3 parameters"""
        self.name = name
        self.height = height
        self.age = age

    def height_increaser(self):
        """A method that increase the size of plant by one"""
        self.height = self.height + 1

    def age_increaser(self):
        """A method that increase the age of plant by one day"""
        self.age = self.age + 1
