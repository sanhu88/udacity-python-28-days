import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Write whatever code you want here!
terry = turtle.Turtle()
terry.width(10)
for color in rainbow:
    terry.pendown()
    terry.color(color)
    terry.forward(100)
    terry.penup()
    terry.right(90)
    terry.forward(10)
    terry.left(90)
    terry.back(100)
    terry.penup()
terry.hideturtle()