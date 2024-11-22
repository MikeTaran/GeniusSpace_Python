# 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        sound = {
            "Cat": "mey",
            "Dog": "bark"
        }
        print(f"The {self.species} says {sound[self.species]}")


animal_1 = Animal("Tom", "Cat", 7)
animal_2 = Animal("Bob", "Dog", 5)
animal_1.make_sound()
animal_2.make_sound()


# 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(f"The Square of Rectangle is {self.height * self.width}")


rect_1 = Rectangle(4, 5)
rect_2 = Rectangle(15, 9)
rect_1.calculate_area()
rect_2.calculate_area()
