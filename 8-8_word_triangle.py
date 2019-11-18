def word_triangle(string):
  n=len(string)
  for letter in range(n):
    print(string[:n])
    n=n-1
  #print(n)
  
word_triangle("kitten")


'''
def word_triangle(word):
  length = len(word)
  for n in range(length):
    print(word[:length - n])
'''