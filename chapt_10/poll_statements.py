filename = 'programming_poll.txt'

with open(filename, 'a') as f_obj:
    active_poll = True
    while active_poll:
        name = input("what is your name? - ")
        response = input("What do you like about programming? - ")
        cont_poll = input("Would someone else like to take the poll? (yes/no) ")
        poll_statement = name.title() + "'s response is: " + response + "\n"

        f_obj.write(poll_statement)
        if cont_poll == "no":
            print("Thanks for taking this poll!")
            active_poll = False
            break
        
    
