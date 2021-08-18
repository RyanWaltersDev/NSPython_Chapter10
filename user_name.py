#!/usr/bin/env python3
'''Ask for user input and write to guest.txt'''

# User input
user_name = input("Welcome! What is your name? ")
print(f"Thank you {user_name}! Your name has been added to the guest list.")

# Append guest.txt
filename = 'guest.txt'
with open(filename, 'a') as file_object:
    file_object.write(f"{user_name}\n")

# Guest book user input
user_date = input("Please enter the date you signed in: ")
user_time = input("And the time: ")
print(f"Thank you {user_name}. You arrived on {user_date} at {user_time}.")

# Append guest_book.txt
filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
    file_object.write(f"{user_name} signed in on {user_date} at {user_time}.\n")
