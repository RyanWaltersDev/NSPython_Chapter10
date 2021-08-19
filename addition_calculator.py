#!/usr/bin/env python3
'''A simple addition calculator with ValueError exception'''

print("Give me two numbers and I will add them together.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q' or first_number == 'Q':
        break
    second_number = input("Second number: ")
    if second_number == 'q' or second_number == 'Q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter a number!")
    else:
        print(f"{first_number} + {second_number} = {answer}")
