def locate_first(sub, string):
    index = 0
    count = 0
    if string.count(sub) ==0:
        print('-1')
    else:
        while index < (len(string) - len(sub) + 1):
            if string[index:index + len(sub)] == sub:
                print(f"{sub} show  {index + 1} in {string} ")
            index += 1
def local_all(sub, string):
    index = 0
    index_list =[]
    if string.count(sub) ==0:
        print('-1')
    else:
        while index < (len(string) - len(sub) + 1):
            if string[index:index + len(sub)] == sub:
                index_list.append(index)
                index +=len(sub)
            else:
                index+=1


        print(f"'{sub}' show  index id {index_list} in '{string} '")
'''
def locate_first(string, sub): 
    index = 0
    while index < (len(string) - len(sub) + 1):
        if string[index : index + len(sub)] == sub:
            return index
        index += 1
    return -1

def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string) - len(sub) + 1:
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches