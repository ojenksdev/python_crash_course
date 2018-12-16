#!/usr/bin/env python3

# Finding averages of a list

list = []
counter = True

while counter == True:
    print("Welcome to the average calculator. Press Q to quit")
    nums = input("Enter a number: ")
    if nums == "Q":
        counter = False
    else:
        nums = int(nums)
        list.append(nums)

def avglist(list):
    return sum(list) / len(list)

list_avg = avglist(list)

print("The average of your list is " + str(list_avg) + ".")
print("Thank you for using this simple script!")
