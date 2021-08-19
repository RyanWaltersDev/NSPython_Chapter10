'''A simple file reader'''

cats_filename = 'cats.txt'
dogs_filename = 'dogs.txt'

try:
    with open(cats_filename) as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)

try:
    with open(dogs_filename) as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)
