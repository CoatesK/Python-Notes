import turtle
import math
pb = turtle.Turtle()
print(pb)

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

pb.fd(48)

pb.begin_poly()
circle(pb, 95)
pb.end_poly()
insi = pb.get_poly()
register_shape("innercircle", insi)

pb.fd(100)
pb.shape(innercircle)

turtle.mainloop
