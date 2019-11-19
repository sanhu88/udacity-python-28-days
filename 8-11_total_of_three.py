#完成
def total_of_three():

	t = float(0)
	for i in [1,2,3]:
		x = input('type the No.'+str(i)+' number(int/float) : ')
		t += float(x)

	print('Total is : '+str(t))
		
total_of_three()

'''
def total_of_three():
   one = input("Enter a number: ")
   two = input("Enter another number: ")
   three = input("Enter a third number: ")
   result = int(one) + int(two) + int(three)
   print(f"{one} + {two} + {three} = {result}")
'''