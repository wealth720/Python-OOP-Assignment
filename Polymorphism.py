# Base Class: Vehicle
class Vehicle:
    def move(self):
        pass  # Abstract method, to be overridden in subclasses

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Bike
class Bike(Vehicle):
    def move(self):
        print("Riding 🚴‍♂️")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Function to demonstrate polymorphism
def vehicle_movement(vehicle):
    vehicle.move()

# Creating objects
car = Car()
bike = Bike()
plane = Plane()

# Testing polymorphism
vehicles = [car, bike, plane]
for v in vehicles:
    vehicle_movement(v)
