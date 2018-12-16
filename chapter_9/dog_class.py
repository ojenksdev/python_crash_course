class Dog():
    """A Class that defines a dog"""

    def __init__(self, name, age):
        """initializing the dogs attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """method that simulates a dog sitting"""
        print("The dog " + self.name + " is now sitting.")


    def roll_over(self):
        """method that simulates a dog rolling over"""
        print("The dog " + self.name + " rolled over!")



rover = Dog('Rover', 1)

rover.sit()
rover.roll_over()
    
