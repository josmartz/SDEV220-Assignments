# Joe Martz
# 4/09/22
# M03_Lab.py
# Gets user input about their vehicle, then displays it

class Vehicle():
    def __init__(self, vehicleType=None):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, vehicleType=None, year=None, make=None, model=None, doors=None, roof=None):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


car = Automobile()
car.vehicleType = input("What type of vehicle is it? ")
car.year = input("What year is it? ")
car.make = input("What make is it? ")
car.model = input("What model is it? ")
car.doors = input("How many doors does it have? ")
car.roof = input("What kind of roof does it have? ")

print(f'''
Vehicle type: {car.vehicleType}
Year: {car.year}
Make: {car.make}
Model: {car.model}
Number of doors: {car.doors}
Type of roof: {car.roof}
      ''')