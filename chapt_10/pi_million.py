filename = 'pi_million_digits.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()


birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")



