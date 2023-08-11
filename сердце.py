from turtle import *
from math import *


def heart():
    hideturtle()
    penup()
    circle(500)
    pendown()

    hideturtle()
    t = 0
    pencolor('red')
    fillcolor('red')
    begin_fill()

    while t < 2 * pi:
        x = 128 * sin(t) ** 3
        y = 8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5)
        goto(x, y)
        t += 0.1

    end_fill()

    done()


heart()
