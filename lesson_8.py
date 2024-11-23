from abc import ABC, abstractclassmethod, abstractmethod


# 1
class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password

    def get_user_info(self):
        return self.__dict__

    def set_user_data(self, data_name, value):
        self.__dict__[f"_{data_name}"] = value


user_1 = User("tom", "tom@gm.net", "1234")
print(user_1.__dict__)
print(user_1.get_user_info())
user_1.set_user_data("name", "Dan")
print(user_1.get_user_info())


# 2
class Shape(ABC):
    @classmethod
    @abstractmethod
    def calculate_area(cls):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 + self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


circle = Circle(5)
print(circle.calculate_area())
rectangle = Rectangle(4, 5)
print(rectangle.calculate_area())
triangle = Triangle(3, 4, 5)
print(triangle.calculate_area())
