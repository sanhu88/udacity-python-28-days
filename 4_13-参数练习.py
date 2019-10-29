import turtle
jack = turtle.Turtle()

jack.speed(0)
def draw_polygon(length,color,sides):
    jack.color(color)
    for side in range(sides):
        jack.forward(length)
        jack.right(360/sides)
#drae_square()

'''
jack.penup()
jack.back(150)
jack.pendown()

draw_square()
jack.forward(100)
draw_square()
jack.forward(100)
draw_square()
'''

for square in range(10):
  jack.pendown()
  draw_polygon(17,"magenta",8)
  jack.penup()
  jack.forward(20)
  jack.left(5)

'''
import turtle
jack = turtle.Turtle()

def draw_shape(length, color, sides):
    jack.color(color)
    for side in range(sides):
        jack.forward(length)
        jack.right(360/sides)

draw_shape(100, "cyan", 5)
'''