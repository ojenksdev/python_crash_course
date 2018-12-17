filename = 'python_learning.txt'

with open(filename) as f_obj:
    content = f_obj.read()
print(content)


with open(filename) as f_obj:
    lines = f_obj.readlines()
    
for line in lines:
    print(line.rstrip())


with open(filename) as f_obj:
    lines = f_obj.readlines()

py_string = ''
for line in lines:
    py_string += line.rstrip()

print("\n" + py_string)
