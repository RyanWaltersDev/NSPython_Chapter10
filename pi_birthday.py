#!/usr/bin/env python3

# One million digits of pi
filename = '../../CC2e resources/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# Check for birthday in first million digits of pi

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print(f"Position in pi: {pi_string.index(birthday)}")
else:
    print("Your birthday does not appear in the first million digits of pi.")

