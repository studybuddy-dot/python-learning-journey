#inheritance example


#parent class

class Vehicle:
    def start(self):
        print("Vehicle is starting")


#child class 1

class Car(Vehicle):
    def drive(self):
        print("Car is moving")


#child class 2

class Bike(Vehicle):
    def ride(self):
        print("Bike is now riding")


#child class 3

class Truck(Vehicle):
    def load(self):
        print("Truck is now loading")


#using classes
c=Car()
c.start()  #from parent
c.drive()

b=Bike()
b.start()
b.ride()

t=Truck()
t.start()
t.load()