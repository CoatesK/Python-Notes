import turtle
pb = turtle.Turtle()
print(pb)
import math
pb.color("green")
pb.pencolor("blue")
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

def arc(t, r):
    """
    Description: A basic way to calculate and draw an arc
    Attributes:
    t - turtle used to draw the arc
    r - radius of the circle the arc comes from
    Returns: an arc turtle object
    """
    arc_length = 2 * math.pi * r * 180 / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = 180 / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

class Petal():
    """
    Description: Represents a petal, any type
    Attributes:
    self.color = a string used to tell what color a petal is
    Returns:
    """
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'This petal is %s' % (self.color)


class Teardrop(Petal):
    """
    Description: a type of PETAL in the teardrop shape
    Attributes:
    self.radius- a float showing the radius of the petal
    Returns - a turtle drawing of the teardrop flower petal type
    """
    def __init__(self, radius, t):
        self.radius = radius

    def __str__(self):
        return 'This petal has a %s pixel radius' % (self.radius)

    def draw(t):
        t.rt(60)
        t.fd(self.radius)
        t.lt(30)
        arc(t,(self.radius /2))
        t.lt(30)
        t.fd(self.radius)
        t.lt(150)

fate = Teardrop(100, pb)
fate.draw()


turtle.mainloop()
