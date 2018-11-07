import turtle
pb = turtle.Turtle()
print(pb)
import math
import random
pb.color("green")
pb.pencolor("black")
pb.shape("turtle")


def randomWalk(t, timeswalked):
    for i in range(timeswalked):
        y = random.randrange(1, 125)
        if y <= 25:
            t.lt(0)
        elif 25 < y <= 50:
            t.lt(90)
        elif 50 < y <= 75:
            t.lt(180)
        elif 75 < y <= 100:
            t.lt(270)
        else:
            r = random.randrange(30, 160)
            angle = random.randrange(1, 359)
            arc(t, r, angle)
        x = random.randrange(50, 200)
        t.fd(x)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

randomWalk(pb, 3)

turtle.mainloop()
