import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.forward(-100)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
  amy.color(prettycolor)
  for _ in [1,2,3,4]:
        amy.right(90)
        amy.forward(50)
  amy.penup()
  amy.forward(100)
  amy.pendown()


#答案
'''
import turtle

amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
# 使线条宽度加粗，以便更容易看到线条
amy.width(5)

# Move back without drawing anything
# 向后移动且不画任何东西
amy.penup()
amy.forward(-140)
amy.pendown()

# Draw three shapes of different colors, with space in between
#绘制三种不同颜色的形状，形状间用空格间隔
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    for side in [1, 2, 3, 4]:
        amy.forward(50)
        amy.right(90)
    amy.penup()
    amy.forward(100)
    amy.pendown()
'''