import turtle

romeo = turtle.Turtle()
romeo.color("violet")
romeo.width(5)
romeo.speed(0)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)



# draw_flower(romeo)
def draw_flower(name):
    for petal in range(6):
        draw_square(name)
        name.right(60)
    name.hideturtle()
draw_flower(romeo)

#方法二
'''
import turtle

romeo = turtle.Turtle()
romeo.color("violet")
romeo.width(5)
romeo.speed(0)

def draw_flower(name):
    for petal in range(6):
        for side in range(4):
            name.forward(100)
            name.right(90)
        name.right(60)
    name.hideturtle()
draw_flower(romeo) 
'''


#课后答案
'''
import turtle

romeo = turtle.Turtle()
romeo.color("violet")
romeo.speed(8)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_flower(some_turtle):
    for petal in range(6):
        draw_square(some_turtle)
        some_turtle.right(60)
    some_turtle.hideturtle()

draw_flower(romeo)
'''