class Employee():
    """Represents an employee"""

    def __init__(self, first, last, salary):
        """initializing the attributes of the class."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, pay_raise=5000):
        """method that adds a raise amount to the salary."""
        self.salary += pay_raise
        return self.salary
        
