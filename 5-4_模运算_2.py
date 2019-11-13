# Write code to draw the staircase
# pattern above.  The modulo operation
# might be useful!

import turtle

amy = turtle.Turtle()
amy.speed(0)
amy.width(4)
amy.color("orange")

for _ in range(10):
    amy.forward(20)
    if _ % 2 == 0:
        amy.left(90)
    else:
        amy.right(90)

'''

import turtle
t = turtle.Turtle()
t.width(5)
t.color("limegreen")

for step in range(21):
  t.forward(10)  # just one!

  # Alternate turning left and right.
  if step % 2 == 0:
    t.left(90)
  else:
    t.right(90)

t.hideturtle()
'''