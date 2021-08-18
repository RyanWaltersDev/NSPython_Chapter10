# Read learning_python.txt.
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# Read learning_python.txt with for loop.
print("\n")
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# Read learning_python.txt by storing in list.
print("\n")
learning_list = ''
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Replacing all instances of 'Python' with 'C'.
print("\n")
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.replace('Python', 'JS')
    print(line.rstrip())
