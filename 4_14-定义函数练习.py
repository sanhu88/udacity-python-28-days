import turtle

amy = turtle.Turtle()
amy.width(3)
amy.speed(0)
# Write a function here that creates a
# turtle and draws a shape with it.
def draw_something(color):
    amy.color(color)
    for count in range(5):
        
        for _ in range(3):
            amy.forward(100)
            amy.right(120)
            
        amy.right(25)
    


# Call the function multiple times.
draw_something("red")
draw_something("yellow")
draw_something("blue")

'''
import turtle

# Write a function here that creates a
# turtle and draws a shape with it.
def triangle_boogie(color, start):
  t = turtle.Turtle()
  t.color(color)
  t.speed(0)
  t.width(5)
  t.right(start)
  for shape in range(6):
    for side in range(3):
      t.forward(100)
      t.right(120)
    t.right(15)
  t.hideturtle()

# Call that function three times.
triangle_boogie("red", 0)
triangle_boogie("orange", 120)
triangle_boogie("blue", 240)
'''