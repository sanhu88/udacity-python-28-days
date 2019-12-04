def starts_with(str1,str2):
	if len(str2) > len(str1):
		print('False')
	#elif str1 in str2 :
	elif str1 == str2[:len(str1)] :
		print('True')
	else:
		print('False')
starts_with('bob', 'bob newby')
starts_with('bill', 'electric bill')

#答案有三种
'''
def starts_with_v1(long, short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True



def starts_with_v2(long, short):
    length = len(short)
    beginning = long[0 : length]
    if beginning == short:
        return True
    else:
        return False


def starts_with_v3(long, short):
    return long[0:len(short)] == short
'''