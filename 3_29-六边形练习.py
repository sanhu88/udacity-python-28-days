import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Write whatever code you want here!
terry = turtle.Turtle()
terry.width(10)
for color in rainbow:
    
    terry.color(color)
    terry.forward(50)
    terry.right(60)
    
terry.hideturtle()