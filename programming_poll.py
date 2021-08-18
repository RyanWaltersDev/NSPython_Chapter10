#!/usr/bin/env python3
'''A simple input prompt asking why a user likes programming'''

user_name = input("Please give us your name: ")
poll = input(f"Hello {user_name}! Give us a reason why you love programming: ")

filename = 'programming_poll.txt'

with open(filename, 'a') as file_object:
    file_object.write(f"{user_name}'s' response: {poll}\n")

print(f"Thank you, your response '{poll}', has been recorded!")
