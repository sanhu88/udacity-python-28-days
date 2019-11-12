import turtle

# This function doesn't quite work.
# It's missing something.
def square(jane):
    for side in range(4):
        jane.forward(20)
        jane.right(90)


# The code below doesn't need editing.
mark = turtle.Turtle()
mark.color("turquoise")
mark.speed(0)
for petal in range(6):
    square(mark)
    mark.right(60)
