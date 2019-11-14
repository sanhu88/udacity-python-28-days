import turtle

amy = turtle.Turtle()
amy.speed(0)
amy.width(2)

mood = "happy8"
 
if mood == "happy":
  amy.color("red")

elif mood == "sad":
	amy.color("blue")
else:
	amy.color("gray")

for side in range(5):
	amy.forward(50)
	amy.right(720/5)
