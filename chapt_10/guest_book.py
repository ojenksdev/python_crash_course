filename = 'guest_book.txt'

with open(filename, 'a') as f_obj:
    active = True
    while active:
        name = input("Hello, what is your name?: ")
        if name != 'q':
            print("Hello there " + name.title())
            f_obj.write(name.title() + "\n")
        else:
            active = False
