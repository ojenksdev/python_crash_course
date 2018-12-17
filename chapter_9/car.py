"""A class that can be used to represent a car."""

class Car():
    """A simple representation of a car"""

    def __init__(self, make, model, year):
        """Initializing the attributes of the car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def odometer_reading(self):
        """Prints out the odometer reading for the car"""
        print("This car has approx. " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        """Updated the odometer reading for the car."""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("It's illegal to roll back an odometer!")

    def increment_odometer(self, miles):
        """Adds miles to the odometer"""
        self.odometer += miles

    def get_descriptive_name(self):
        """Prints out a proper description of the car"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()


