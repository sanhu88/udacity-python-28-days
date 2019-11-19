def good_length(pwd):
	return 8<len(pwd)<64
print(good_length("2short"))
print(good_length("nice password, yo"))
print(good_length("This is really much too long for a password. I mean, it's really secure, but I don't want to type this much every time I log in, okay?"))