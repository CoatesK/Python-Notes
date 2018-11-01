import turtle
t = turtle.Turtle()
def square(t, length, color):
    for i in range (4):
        t.color(color)
        t.fd(length)
        t.lt(90)


square(t, 100, "green")
turtle.mainloop()
