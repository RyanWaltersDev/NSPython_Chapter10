#!/usr/bin/env python3
'''A simple input prompt asking why a user likes programming'''

# User input
user_name = input("Please give us your name: ")
poll = input(f"Hello {user_name}! Give us a reason why you love programming: ")

# Append file with response
filename = 'programming_poll.txt'

with open(filename, 'a') as file_object:
    file_object.write(f"{user_name}'s' response: {poll}\n")

# Print message thanking user
print(f"Thank you, your response '{poll}', has been recorded!")
