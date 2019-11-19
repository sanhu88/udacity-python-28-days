def total_length(your_list):
	t_len = int(0)
	
	for single in your_list:
		length = len(single)
		t_len += length
	print("total_length of list is ",t_len)

total_length(["dhqduhwq","dssd"])

'''
def total_length(strings):
    total = 0
    for s in strings:
        total = total + len(s)
    return total
'''
'''
def total_length(strings):
    return sum(map(len, strings))
'''