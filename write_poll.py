'''Creates the programming_poll.txt file and can also erase its contents.'''

filename = 'programming_poll.txt'
with open(filename, 'w') as file_object:
    file_object.write("Poll responses: \n")
