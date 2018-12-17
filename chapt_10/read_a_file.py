def read_contents(filename):
    """Read the contents of a file"""

    try:
        with open(filename, 'r') as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        print("Sorry, but the file " + filename + " appears to be missing.")
    else:
        print(content)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_contents(filename)

        
        

   
        
