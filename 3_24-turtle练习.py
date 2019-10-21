import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(2)

# Move back without drawing anything
amy.penup()
amy.back(80)


# mathod one
colors =["red","orange","yellow"]
for color in colors :
    
    
    amy.color(color)
    amy.forward(20)
    amy.pendown()
    amy.forward(40)
    amy.penup()



'''method two
# Draw a red line
amy.pendown()
amy.color("red")
amy.forward(40)

# Move forward without drawing anything
amy.penup()
amy.forward(30)
# Draw an orange line
amy.pendown()
amy.color("orange")
amy.forward(40)
# Move forward without drawing anything
amy.penup()
amy.forward(30)

# Draw a yellow line
amy.pendown()
amy.color("yellow")
amy.forward(40)
'''


# 答案
'''
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

# Draw three lines of different colors, with space in between
#绘制三条不同颜色的线，线与线之间用空格间隔
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    amy.forward(50)
    amy.penup()
    if prettycolor != "yellow":
        amy.forward(50)
    amy.pendown()
'''