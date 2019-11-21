#以下未完成，任意字符检测
def count_ch(string, target):
	index = 0
	total = 0
	lenth_chart = len(target)
	#while index < len(string):
	for _ in string:
		if string[index:index+len(target)] == target:
		  total += 1
		index += 1
	print(target,"show ",total," times in",string)
count_ch("oxen and foxen all live in boxen","l")		

#count 函数 直接返回
def count_any(str,chart):
	print(chart,"show ",str.count(chart)," time(s) in",str)
count_any("oxen and foxen all live in boxen","li")

