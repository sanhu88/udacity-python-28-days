def until_dot(string):
	index =0
	while string[index] != ".":
		index +=1
		print(string[:index])
	print("No dots here")	
until_dot("This is a sentence. This is another.")
until_dot("No dots here")		