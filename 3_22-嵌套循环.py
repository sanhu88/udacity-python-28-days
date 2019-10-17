import turtle

links = [1, 2, 3, 4, 5, 6, 7, 8]
sides = [1, 2, 3, 4, 5, 6]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')
weaver.speed(2)

# Move back so the chain is centered.
weaver.penup()
weaver.back(80)
weaver.pendown()

for link in links:
    # Draw a hexagon.
    for side in sides:
        weaver.forward(40)
        weaver.right(60)

    # Scoot over to the next link.
    weaver.penup()
    weaver.right(60)
    weaver.forward(60)
    weaver.pendown()

weaver.hideturtle()