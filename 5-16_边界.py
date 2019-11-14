def in_bounds(x, y):
    # Change the next line!
    #x > -175 and  x < 175 and y > -175 and  y < 175
    return ( x > -175 and  x < 175 and y > -175 and  y < 175)

rainbow = ["red", "orange", "yellow",
           "green", "blue", "purple"]

import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.width(5)
t.color(random.choice(rainbow))

for step in range(400):
    t.forward(30)
    t.right(random.randint(-45, 45))
    if not in_bounds(t.xcor(), t.ycor()):
        # We're going out of bounds!
        # Move the turtle home and pick
        # a new direction and color.
        t.penup()
        t.home()
        t.pendown()
        t.right(random.randint(0, 360))
        t.color(random.choice(rainbow))

'''
def inBounds(x, y):
    return (x > -175 and x < 175 and y > -175 and y < 175)

'''
def inBounds(x, y):
    return (-175 < x < 175) and (-175 < y < 175)
'''
