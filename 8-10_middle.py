#未完成
import math
def middle(a,b,c):
	a_ord = ord(a[0])
	b_ord = ord(b[0])
	c_ord = ord(c[0])
	
	max_ord = max(a_ord,b_ord,c_ord)
	min_ord = min(a_ord,b_ord,c_ord)

	print(max_ord)

	print('\n')

	print(min_ord)

middle('A','c','B')

'''
def middle(a, b, c):
    if b >= a >= c or c >= a >= b:
       return a
    if a >= b >= c or c >= b >= a:
       return b
    if a >= c >= b or b >= c >= a:
       return c
'''