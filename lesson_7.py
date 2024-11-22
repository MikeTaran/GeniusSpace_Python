# 1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, year, car_type):
        super().__init__(make, model, year)
        self.car_type = car_type

    def car_ride(self):
        print(f"The {self.make} {self.model} {self.year} is {self.car_type} model")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, moto_type):
        super().__init__(make, model, year)
        self.moto_type = moto_type

    def moto_ride(self):
        print(f"The {self.make} {self.model} {self.year} is {self.moto_type} model")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def bike_ride(self):
        print(f"The {self.make} {self.model} {self.year} is {self.bike_type} model")


car = Car("Nissan", "X-Trail", 2012, "off-road")
moto = Motorcycle("Harley", "Out-road", 2015, "off-road")
bike = Bicycle("A-Tech", "Waterfall", 2017, "city-street")

print(car.__dict__)
print(moto.__dict__)
print(bike.__dict__)

car.car_ride()
moto.moto_ride()
bike.bike_ride()
