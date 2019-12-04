def is_substring(short_str,long_str):
	index = 0
	if len(short_str) > len(long_str):
		print('False')
	elif short_str == long_str:
	  print('True')
	else:
	  while index < (len(long_str) - len(short_str) + 1):
			if long_str[index : index + len(short_str)] == short_str:
				print('True')
			else:
			  print('False')
			break
			index += 1
	
	     


is_substring('bad', 'abracadabra')
is_substring('dab', 'abracadabra')
is_substring('pony', 'pony')
is_substring('', 'balloon')
is_substring('balloon', '')