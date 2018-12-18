import json

filename = 'fav_number.json'

try:
    with open(filename) as f_obj:
        fav_num = json.load(f_obj)
except FileNotFoundError:
    number = input("What is your favorite number? -")
    filename = 'fav_number.json'

    with open(filename, 'w') as f_obj:
        json.dump(int(number), f_obj)
else:
    print("I know your favorite number! It's " + str(fav_num) + ".")





