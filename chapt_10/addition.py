# Addition program -- Adds two numbers

print("Give me two numbers and I'll add them together. ")
print("Type 'q' to quit")

while True:
    first_num = input("\nFirst Number: ")
    if first_num == "q":
        break
    second_num = input("\nSecond Number: ")
    if second_num == "q":
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("I can only add numbers!")
    else:
        print("The answer is " + str(answer))
        
        
