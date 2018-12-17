filename = "prince_henry_the_navigator.txt"

with open(filename, encoding='utf-8') as f_obj:
    content = f_obj.read()

    find_the = content.lower().count('the')
    print("The word 'the' appears approximately " + str(find_the) + " times in the text.")
    
