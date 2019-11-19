def starts_with(str1,str2):
	str2_len = len(str(str2));
	return str(str1)[:int(str2_len)] == str(str2)

print(starts_with(888888,88))
print(starts_with("test","te"))
print(starts_with("98sz",98))

#答案一
'''
def starts_with_v1(long ,short):
	for position in range(len(short)):
		if long[position] != short[position]:
			return False
	return True
print(starts_with_v1("apple","app"))
'''

#答案二
'''
def starts_with_v2(long ,short):
	length = len(short)
	beginning = long[0:length]
	if beginning == short:
		return True
	else:
		return False
print(starts_with_v2("apple","app"))
'''

#答案三，简化于答案二
'''
def starts_with_v3(long ,short):
	return long[:len(short)] == short
print(starts_with_v2("apple","app"))
'''