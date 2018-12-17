filename = "alice.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # count the approx. number of words in the text file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has around " + str(num_words) + " words in it.")
