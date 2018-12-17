from users import User


class Privileges():
    """Class describing the privileges for an admin"""
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        """initializing the attributes for the privileges class"""
        self.privileges = privileges

    def show_privileges(self):
        """method that prints the privileges of an admin user."""
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print("\t-" + privilege)        

    

class Admin(User):
    """Admin class that has additional privileges than a standard user."""
    def __init__(self, first_name, last_name, age, profession, location):
        """initializing the attributes from the parent class."""
        super().__init__(first_name, last_name, age, profession, location)
        self.privileges = Privileges()
