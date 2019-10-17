import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
# 使线条宽度加粗，以便更容易看到线条
amy.width(5)

# Move back without drawing anything
# 向后移动且不画任何东西
amy.penup()
amy.back(140)
amy.pendown()

# Draw three red lines, with space in between
#绘制三条红线，线与线之间用空格间隔
for line in [1, 2, 3]:
    amy.color("red")
    amy.forward(50)
    amy.penup()
    if line != 3:
        amy.forward(50)
    amy.pendown()