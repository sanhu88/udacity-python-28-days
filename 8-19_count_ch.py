def count_ch(str,chart):
	counter = 0
	lenth_chart = len(chart)
	for _ in str:
		if str[:len(chart)] == chart:
			counter += 1
	print(chart,"show ",counter," times in",str)
count_ch("oxen and foxen all live in boxen","li")		


