import json

# Reads in a number value from a different program

filename = 'fav_number.json'

with open(filename) as f_obj:
    fav_num = json.load(f_obj)
print("I know your favorite number! It's " + str(fav_num) + ".")
