# Fill out the function bead_color.
# It should return color names so that the
# chain of beads will alternate among red,
# green, and blue.

import turtle

def bead_color(num):
    if num % 3 == 0:
        return "red"
    if num % 2 == 0:
        return "blue"
    else:
        return "green"

def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)

t = turtle.Turtle()
t.speed(0)
t.width(2)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

# Draw ten beads.
for n in range(10):
    t.color(bead_color(n))
    bead(t)
    t.forward(40)

'''
def beadColor(num):
    if num % 3 == 0:
        return "red"
    if num % 3 == 1:
        return "green"
    if num % 3 == 2:
        return "blue"
'''

'''
def beadColor(num):
    if num % 3 == 0:
        return "red"
    else:
        if num % 3 == 1:
            return "green"
        else:
            return "blue"

'''
如果 num 是整数，num % 3 唯一可能的值是 0、1 和 2。
因此在此函数结束时，当我们处理了 0 和 1 的情形，我们知道唯一剩下的可能性是 2。
因此，我们可以直接使用 else:，而不是第三个 if 语句。
'''