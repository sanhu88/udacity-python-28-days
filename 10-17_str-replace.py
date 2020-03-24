def remove_substring(original_str,delete_str):
    list_save =[]
    #print(len(original_str))
    #print(len(delete_str))
    index = 0
    #for index in range(len(original_str)):
    while index < len(original_str):
        if original_str[index:index+len(delete_str)] == delete_str:
            index += len(delete_str)
            #print(index)
        else:
            list_save.append(original_str[index])
            #print(index)
            index+=1
    return("".join(list_save))

print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
print(remove_substring('I am NOT learning to code.', 'NOT '))