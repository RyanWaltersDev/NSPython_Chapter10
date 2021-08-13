with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

file_path = ("/home/ryan/Documents/No Starch Python/Projects/chapter_ten/"
    "text_files/pi_digits.txt")
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)
