import random
letters = ['a'] * 100
b = random.randint(0, 99)
letters[b] = 'b'
letters = "".join(letters)

# Search for the letter b in the string.
# How many times will this print "Not yet" ?
print(letters)
print("Looking for 'b' ...")
pos = 0
while letters[pos] != 'b':
    pos += 1
    print("Not yet")
    print(pos)
print("Found it!")