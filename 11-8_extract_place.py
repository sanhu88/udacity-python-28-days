def extract_place(str):
  index = 0
  n =0
  m =0
  for index in range(len(str)):
    if '_' == str[index:index+1]:
      n = index
      break
      index +=1
  print(n)
  for index in range(len(str[n:])):
    if '_' == str[index:index+1]:
      m = index
      
      index +=1
  return str[n+1:m]


print(extract_place("2018-06-06_MountainView_16:20:00.jpg"))
print(extract_place("2018-06-06_Ohio_16:20:00.jpg"))

'''
#答案
def extract_place(filename):
  retuen filename.split('_')[1]

def extract_place(filename):
  one = filename.find['_']
  left = filename[one+1:]
  second = filename.find['_']
  return left[:second]
'''