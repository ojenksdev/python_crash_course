from random import randint


class Die():
    """Class representing a dice"""

    def __init__(self, sides=6):
        """initializing the attributes of the die class"""
        self.sides = sides

    def roll_die(self):
        """method that simulates rolling a dice"""
        roll = randint(1,6)
        print("This dice has " + str(self.sides) + " sides.")
        print("You rolled a " + str(roll))


six_sided = Die()
six_sided.roll_die()
        

ten_sided = Die(sides=10)
ten_sided.roll_die()
