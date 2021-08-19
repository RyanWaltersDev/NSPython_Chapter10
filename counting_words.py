'''A simple word counter'''

the_vault = 'the_vault.txt'
wotw = 'war_of_the_worlds.txt'
on_liberty = 'on_liberty.txt'

with open(the_vault) as f:
    contents = f.read()
    the_count = contents.lower().count('the ')
print(f"The Valut by Murray Leintser contains 'the' {the_count} times!")

with open(wotw) as f:
    contents = f.read()
    the_count = contents.lower().count('the ')
print(f"War of the Worlds by H.G. Wells contains 'the' {the_count} times!")

with open(on_liberty) as f:
    contents = f.read()
    the_count = contents.lower().count('the ')
print(f"On Liberty by John Stuart Mill contains 'the' {the_count} times!")
