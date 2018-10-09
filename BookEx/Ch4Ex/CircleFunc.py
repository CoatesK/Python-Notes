import turtle
t = turtle.Turtle()
t.shape("turtle")

import math

def circle(t, r, color):
    '''
    Makes the turtle make a circle, after the user enters the radius of
    the circle.

    '''
    t.color(color)
    C = 2 * r * math.pi
    t.fd(C)
    t.lt(90)
    n = 360


circle(t, 50, "red")
turtle.mainloop()
