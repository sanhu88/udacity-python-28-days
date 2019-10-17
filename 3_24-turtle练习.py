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