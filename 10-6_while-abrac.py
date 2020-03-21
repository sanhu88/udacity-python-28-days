s = "abracadabra"
# Add your code here
import time
index =0
while index < len(s):
    print(s[:len(s)-index])
    index +=1
    time.sleep(1)

'''
s = "abracadabra"
index = len(s)
while index > 0:
    print(s[:index])
    index -= 1
'''