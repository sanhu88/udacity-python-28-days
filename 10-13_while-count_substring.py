def count_substring(long_str,target):
	index = 0
	for index in range(len(long_str)-len(target)+1):
		if long_str[index:index+len(target)] == target:
			index+=1
	print('{trage} is show in {long_str} with {index} times'.format(trage,long_str,index))
count_substring('love, love, love, all you need is love', 'love')

'''
def count_substring_v1(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
        index += 1    # <- look here
    return count

def count_substring_v2(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
            index += len(target)   # <- look here
        else:
            index += 1
    return count
'''