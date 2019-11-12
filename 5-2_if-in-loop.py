import turtle
jack = turtle.Turtle()
jack.width(5)

jack.color("yellow")
for side in range(4):
    if side == 1:
        jack.color("blue")
    if side == 2:
        jack.color("yellow") 
    jack.forward(100)
    jack.right(90)