
class Garden_Manager:
    def __init__(self, garden_name):
        self.__lst.append(garden_name)

class Garden:
    def __init__(self, name, flower, flowering, prize):
        self.__name = name
        self.__lst_flower = []
        self.__lst_flowering = []
        self.__lst_prize = []
        self.__lst_flower.append(flower)
        self.__lst_flowering.append(flowering)
        self.__lst_prize.append(prize)

    def get_name(self):
        print(self.__name)


class Base_Plant:
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
        """A method that return the height of the plant"""
        return (self.__height)

    def get_age(self):
        """A method that return the age of the plant"""
        return (self.__age)

    def get_name(self):
        """A method that return the name of the flower"""
        return (self.__name)

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


class Flower(Base_Plant):
    """Creating a flower, a specialised type of Base_Plant"""
    def __init__(self, name, height, age, color):
        """A specialised class with a color parameter"""
        super().__init__(name, height, age)
        self.__color = color

    def get_info(self):
        n = self.get_name()
        h = self.get_height()
        a = self.get_age()
        print(f"{n} (Flower): {h} cm, {a} days, {self.get_color()}")

    def bloom(self):
        """Make the flower bloom"""
        print(f"{self.get_name()} is blooming beautifully !")

    def get_color(self):
        """Gives the color of the actual flower"""
        return (self.__color)


class Tree(Base_Plant):
    def __init__(self, name, height, age, trunk_diameter):
        """Creates a Tree, with a base plant plus a diameter"""
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter

    def get_info(self):
        n = self.get_name()
        h = self.get_height()
        a = self.get_age()
        d = "cm diameter"
        print(f"{n} (Tree): {h} cm, {a} days, {self.get_diameter()} {d}")

    def get_diameter(self):
        """Gives the diameter of the requested tree"""
        return (self.__trunk_diameter)

    def produce_shade(self):
        """Gives the shade """
        res = (int(self.get_diameter()) * 1.56)
        print(f"{self.get_name()} provides {int(res)} square meters of shade ")


class Vegetable(Base_Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.__harvest_season = harvest_season
        self.__nutritional_value = nutritional_value

    def get_info(self):
        name = self.get_name()
        height = self.get_height()
        age = self.get_age()
        print(f"{name} (Vegetables): {height} cm, {age} days, {self.get_hr()}")
        print(f"{name} is rich in {self.get_nutritional_value()}")

    def get_nutritional_value(self):
        return (self.__nutritional_value)

    def get_hr(self):
        return (self.__harvest_season)


class Factory():
    """A factory class to create a function create plant"""
    def create_plant(my_data):
        """A create plant function to make a lot of plant"""
        return (Base_Plant(my_data[0], my_data[1], my_data[2]))


if (__name__ == "__main__"):
    test = Garden("Alice", "rose", "white", "purple")
    test.get_name()
