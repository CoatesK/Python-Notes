import turtle
pb = turtle.Turtle()
print(pb)
import math
pb.color("green")
pb.pencolor("black")
pb.shape("turtle")

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumfrence = 2 * math.pi * r
    n = int(circumfrence / 2) +1
    length = circumfrence / n
    polygon(t, n, length)

def pulse(turtle):
    '''
    This function draws a pulse that is shown in the .pdf file.

    parameters: turtle - Turtle object
    Returns: None
    '''
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)
    turtle.rt(90)
    turtle.fd(50)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)

def house(turtle, length):
    '''
    This function draws the house shown in the .pdf file.

    parameters: turtle - Turtle object
                length - side length

    Returns: None
    '''
    turtle.fd(length)
    turtle.lt(90)
    turtle.fd(length)
    turtle.rt(90)
    for i in range(5):
        turtle.lt(120)
        turtle.fd(length)
    turtle.lt(30)
    turtle.fd(length)
    turtle.lt(90)
    turtle.fd(length)

def manyHouses(turtle, length, number):
    '''
    This function uses the house() function to draw n houses with the given
    length. These houses should be dettached from each other.

    parameters: turtle - Turtle object
                length - The side length
                number - The number of houses to be drawn.

    '''
    for i in range(number):
        house(turtle, length)
        turtle.penup
        turtle.fd(length)
        turtle.pendown




turtle.mainloop()
