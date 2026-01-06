
class Secure_Plant:
    def __init__(self, name, height, age):
        """A class for the creation of Plant, with 3 parameters"""
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Created {self.__name} ({self.__height}, {self.__age})")

    def grow(self):
        """A method that increase the size of plant by seven because
        its a week simulation and we admit that it grows 1cm a day and print
        the size of how many cm it grows"""
        self.__height += 7
        print("Growth this week 7cm")

    def aging(self):
        """A method that increase the age of plant by one week"""
        self.__age += 7

    def get_info(self):
        """A method that let u know the status of the plant"""
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def get_height(self):
        """A method that displays the height of the plant"""
        return (self.__height)

    def get_age(self):
        """A method that displays the age of the plant"""
        return (self.__age)

    def set_height(self, value):
        """A method that allows yout to modify the height of the plant"""
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__height = value
        print("Height updated", value, "[OK]")

    def set_age(self, value):
        """A method that allows yout to modify the age of the plant"""
        if (value < 0):
            print(f"Error Negative Number [{value} < 0]")
            return
        self.__age = value
        print("Age updated", value, "[OK]")


class Factory():
    """A factory class to create a function create plant"""
    def create_plant(my_data):
        """A create plant function to make a lot of plant"""
        return (Secure_Plant(my_data[0], my_data[1], my_data[2]))