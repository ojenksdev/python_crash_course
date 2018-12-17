from car import Car

class Battery():
    """Modeling a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initializing the battery's attributes."""
        self.battery_size = battery_size

    def get_range(self):
        """Prints out the range of the electric cars battery."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Increases the battery size and range."""
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print("The battery is already upgraded to 85-kWh.")

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a battery size of " + str(self.battery_size) + "-kWh.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

