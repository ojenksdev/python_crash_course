def count_words(filename):
    """Count the number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        with open('errors.txt', 'a') as file_ob:
            msg = "Sorry, the file " + filename + " was not found."
            errors = file_ob.write(msg)
        pass
    else:
        words = content.split()
        num_words = len(words)
        print("The file " + filename + " contains around " + str(num_words) +
              " words.")
        


filenames = ['alice.txt', 'wizard_of_oz.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)
