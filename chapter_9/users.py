class User():
    """Creating a class that stores user information"""

    def __init__(self, first_name, last_name, age, profession, location):
        """initializing the attributes of the user class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.location = location
        self.login_attempts = 0


    def describe_user(self):
        """method that describes user"""
        print("-----User Information-----")
        print("First Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Profession: " + self.profession.title())
        print("Location: " + self.location.title())

    def increment_login_attempts(self):
        """Adds 1 to the amount of times a user tries to login incorrectly"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts"""
        self.login_attempts = 0


    def greet_user(self):
        """method that greets the user"""
        print("\nHello there " + self.first_name.title() + "!")






        
