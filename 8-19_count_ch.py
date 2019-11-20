#以下未完成，任意字符检测
def count_ch(str,chart):
	counter = 0
	lenth_chart = len(chart)
	for _ in str:
		if str[:len(chart)] == chart:
			counter += 1
	print(chart,"show ",counter," times in",str)
count_ch("oxen and foxen all live in boxen","li")		

#count 函数 直接返回
def count_any(str,chart):
	print(chart,"show ",str.count(chart)," time(s) in",str)
count_any("oxen and foxen all live in boxen","li")

