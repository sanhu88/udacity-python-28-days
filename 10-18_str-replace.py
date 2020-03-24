def replace_substring(original_str,delete_str,replace_str):
    list_save =[]
    #print(len(original_str))
    #print(len(delete_str))
    index = 0
    #for index in range(len(original_str)):
    while index < len(original_str):
        if original_str[index:index+len(delete_str)] == delete_str:
            list_save.append(replace_str)
            index += len(delete_str)
            #print(index)
        else:
            list_save.append(original_str[index])
            #print(index)
            index+=1
    return("".join(list_save))


print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))

'''
def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replacement)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)
'''