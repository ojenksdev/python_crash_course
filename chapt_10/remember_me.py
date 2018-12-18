import json


def get_stored_username():
    """Retrieves the username from a file"""
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Gets a new username if one doesn't exist"""
    username = input("What is your name? - ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
   

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    verify_user = input("Is " + username + " your username? (yes/no) ")
    if verify_user == "no":
        username = get_new_username()
        print("We'll remember you when you come back " + username + "!")
    elif username:
        print("Welcome back " + username + "!")
    else:
       username = get_new_username()
       print("We'll remember you when you come back " + username + "!")
            
greet_user()
