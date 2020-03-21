def count_character(string, target):
    total = 0
    index =0
    while index < len(string):
        if target == string[index:index+len(target)]:
            total += 1
        index +=1
    return total

print(count_character("bonobon", "on"))
print(count_character("bonobon", "o"))

'''
def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total
'''