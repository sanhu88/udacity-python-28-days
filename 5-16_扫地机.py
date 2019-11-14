import turtle
import random
import vacuumsetup

def vacuumTurtle():
    # Create a vacuum turtle.
    t = turtle.Turtle()
    t.width(30); t.speed(0)
    t.color("white")
    return t

def nearWall(t):
    # Is the turtle near a wall?
    x, y = t.pos()
    bounds = 100 - t.width() * 2/3
    return not (-bounds < x < bounds
            and -bounds < y < bounds)

def cleanRoom():
    t = vacuumTurtle()
    # Write your code here!
    
    for step in range (200):
        if not nearWall(t):
            t.forward(step)
            t.right(90)
        
        
    
        
        

# Don't remove this function call!
cleanRoom()

'''
#第二种自己的方法，随机乱窜
import turtle
import random
import vacuumsetup

def vacuumTurtle():
    # Create a vacuum turtle.
    t = turtle.Turtle()
    t.width(30); t.speed(0)
    t.color("white")
    return t

def nearWall(t):
    # Is the turtle near a wall?
    x, y = t.pos()
    bounds = 100 - t.width() * 2/3
    return not (-bounds < x < bounds
            and -bounds < y < bounds)

def cleanRoom():
    t = vacuumTurtle()
    # Write your code here!
    
    for step in range (5000):
        t.forward(5)
        if  nearWall(t):
            t.back(5)   #这一步很重要，不然会越界了
            t.right(random.choice([-70,70]))
        

# Don't remove this function call!
cleanRoom()
'''

'''
#应该还有第三种，使 turtle 来回移动，从一边到另一边，并在靠近墙壁时掉头。
#以下没完成
import turtle
import random
import vacuumsetup

def vacuumTurtle():
    # Create a vacuum turtle.
    t = turtle.Turtle()
    t.width(10); t.speed(0)
    t.color("white")
    return t

def nearWall(t):
    # Is the turtle near a wall?
    x, y = t.pos()
    bounds = 100 - t.width() * 2/3
    return not (-bounds < x < bounds
            and -bounds < y < bounds)

def cleanRoom():
    t = vacuumTurtle()
    # Write your code here!
    
    for step in range (800):
        
        if not nearWall(t):
            t.forward(1)
        else:
            #t.right(random.choice([-90,90]))
            t.back(5)
            #t.right(-90)
            t.forward(1)
            t.right(-90)
            
            
            
        
        
    
        
        

# Don't remove this function call!
cleanRoom()

'''