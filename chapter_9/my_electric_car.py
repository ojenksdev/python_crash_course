from car import Car
from electric_car import ElectricCar


my_toyota = Car('toyota', 'camry', 2015)
print(my_toyota.get_descriptive_name())


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
