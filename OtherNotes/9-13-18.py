import random
import turtle

x = random.randrange(0, 100)
a = random.randrange(-90, 90)
c = random.choice("red", "green", "orange", "yellow")

t = turtle.Turtle()
def randomWalk(t, n):
    for i in range(n):
        t.color(random.choice(c))
        t.fd(random.randrange(x))
        t.rt(random.randrange(a))

randomWalk(t, 50)
turtle.mainloop()
