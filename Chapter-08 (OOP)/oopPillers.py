#Abstruction
"""Showing only essential details, hiding internal complexity. For example you use Insta 
    without knowing its backend code"""

#Encapsulation
"""Wrapping data+method inside a single unit called class.
    Data is protected using private variables"""

#Inheritance
"""A mechanism that allows a new class to acquire the attributes and methods of an existing class"""

class vehicle:
    @staticmethod
    def start():
        print("Vehicle started")

class car(vehicle):
    @staticmethod
    def run():
        print("Vehicle is running")

class bike(vehicle):
    @staticmethod
    def stop():
        print("Vehicle stopped running")

c1 = car()
c1.start()
c1.run()

b1 = bike()
b1.start()
b1.stop()

#Polymorphism
"""Polymorphism means "many forms". In programming,
 it allows the same interface, function, or operator to work with different data types or classes."""

class cow:
    def sound(self):
        print("Mooo")

class cat:
    def sound(self):
        print("Meow")

class dog:
    def sound(self):
        print("Gheu")

animal = [cow(),cat(),dog()]

print("\nUsing polymorphism:")

for a in animal:
    a.sound()