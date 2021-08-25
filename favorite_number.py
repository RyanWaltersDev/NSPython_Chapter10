#!/usr/bin/env python3
import json


def get_favorite_number():
    '''Get user's favorite number, if it exists'''
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number():
    '''Retrieve a favorite number from user'''
    filename = 'favorite_number.json'
    while True:
        number = input("What is your favorite number? ")
        try:
            number = int(number)
        except ValueError:
            print("Please enter a number!")
        else:
            with open(filename, 'w') as f:
                json.dump(number, f)
            return number
            break

def greet_user():
    '''Tells user favorite number, or asks for it if non-existent'''
    number = get_favorite_number()
    if number:
        print(f"We know your favorite number, it's {number}!")
    else:
        number = get_new_number()
        print(f"Your favorite number is {number}! We will remember next time.")

greet_user()
