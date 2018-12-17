filename = 'guest_name.txt'

with open(filename, 'w') as f_obj:
    name = input("Hello, what is your name?: ")
    f_obj.write(name)
