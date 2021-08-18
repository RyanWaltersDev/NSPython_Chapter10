'''Creates the programming_poll.txt file and can also erase its contents.'''

# CAREFUL! RUNNING THIS CODE WILL ERASE THE CONTENTS OF PROGRAMMING_POLL.TXT
filename = 'programming_poll.txt'
with open(filename, 'w') as file_object:
    file_object.write("Poll responses: \n")
