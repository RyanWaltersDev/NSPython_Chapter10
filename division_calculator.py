#!/usr/bin/env python3
'''try-except block for ZeroDivisionError'''

#try:
    #print(5/0)
#except ZeroDivisionError:
    #print("Why would you do that? Dividing by zero are you kidding?")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q' or first_number == 'Q':
        break
    second_number = input("Second number: ")
    if second_number == 'q' or second_number == 'Q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
