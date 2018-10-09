import turtle
t = turtle.Turtle()
def polygon(t, sides, length, color):
    '''
    makes the turtle make a polygon with a set length
    and number of sides

    t - turtle; this turtle does the drawing
    length - integer; this is the side length for
    the polygon
    sides - integer; this determines the number of sides
    '''
    angle = 360/sides
    for i in range(sides):
        t.color(color)
        t.fd(length)
        t.lt(angle)



polygon(t, 5, 200, "blue")
turtle.mainloop()
