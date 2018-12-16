class Restaurant():
    """A class describing a restaurant"""

    def __init__(self, name, cuisine_type):
        """initializing the attributes of the restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints a message describing the restaurant"""
        print("The name of the restaurant is " + self.name.title())
        print("The food they make is " + self.cuisine_type.title())


    def open_restaurant(self):
        """method that announces the restaurant is open"""
        print(self.name.title() + " is open for business!")


picasso = Restaurant('picasso', 'italian')
picasso.describe_restaurant()
picasso.open_restaurant()

marshalls = Restaurant('marshalls', 'BBQ')
marshalls.describe_restaurant()
