import turtle
pb = turtle.Turtle()
pb.color("green")
pb.pencolor("black")
pb.shape("turtle")

def countdown(n):
        if n <= 0:
            print("Blastoff!")
        else:
            print(n)
            countdown(n - 1)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    t.bk(length / 2)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(2 * n)

draw(pb, 12, 6)

turtle.mainloop()
