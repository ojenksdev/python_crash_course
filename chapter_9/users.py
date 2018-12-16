class User():
    """Creating a class that stores user information"""

    def __init__(self, first_name, last_name, age, profession, location):
        """initializing the attributes of the user class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.location = location


    def describe_user(self):
        """method that describes user"""
        print("-----User Information-----")
        print("First Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Profession: " + self.profession.title())
        print("Location: " + self.location.title())


    def greet_user(self):
        """method that greets the user"""
        print("\nHello there " + self.first_name.title() + "!")



john_doe = User('john', 'doe', 30, 'web developer', 'austin')
john_doe.describe_user()
john_doe.greet_user()
        
