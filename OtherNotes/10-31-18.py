import turtle
from math import pi

t = turtle.Turtle()

def segment(t, length):
    t.penup()
    t.fd(length)

def ring(t, r, color):
    circumference = 2 * pi * r
    n = 50
    length = circumference / n
    t.color(color)
    t.circle(circumference)




def firstThree(t, length, r, n):
    if n == 1:
        color = "blue"
    elif n == 2:
        color = "black"
    elif n == 3:
        color = "red"
    for i in range(3):
        if n == 4:
            segment(t, length)
        else:
            segment(t, length)
            t.rt(90)
            t.penup()
            t.fd(r*6)
            t.lt(90)
            t.pendown()
            ring(t, r, color)
            t.penup()
            t.lt(90)
            t.fd(r*6)
            t.rt(90)
            t.pendown()
            n += n + 1

firstThree(t, 220, 20, 1)


'''
import turtle

myTurtle = turtle.Turtle(shape="turtle")
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(60,60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)
'''

turtle.mainloop()
