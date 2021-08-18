'''Write files guest.txt and guest_book.txt'''

# CAREFUL! RUNNING THIS CODE WILL ERASE PREVIOUS CONTENT STORED IN FILES
filename = 'guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(f"Guest list: \n")

filename = 'guest_book.txt'
with open(filename, 'w') as file_object:
    file_object.write(f"Guest book: \n")
