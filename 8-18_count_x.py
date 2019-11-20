def count_x(str):
	counter = 0
	for _ in str:
		if _ == "x" or _ == "X":
			counter += 1
	print("X or x show ",counter," times.")
count_x("oxen and foxen all live in boxen")

#答案
'''
def count_ch(string, target):
    total = 0
    for ch in string:
        if ch == target:
            total += 1
    return total
'''