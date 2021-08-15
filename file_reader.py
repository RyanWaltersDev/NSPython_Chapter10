#File reading using relative path.
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# File reading using absolute path.
file_path = ("/home/ryan/Documents/No Starch Python/Projects/chapter_ten/"
    "text_files/pi_digits.txt")
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

# File reading line by line
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Store lines in a list and print
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
