#!/usr/bin/env python3
import json

def get_stored_username():
    '''Get stored username if available.'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    '''Greet the user by name.'''
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
        while True:
            answer = input("Is this name correct? [Y/N] ")
            if answer == 'Y' or answer == 'y':
                break
            elif answer == 'N' or answer == 'n':
                print("No problem, let's fix that.")
                username = get_new_username()
                print(f"We'll remember you next time, {username}!")
                break
            else:
                print("Please enter a valid response.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
