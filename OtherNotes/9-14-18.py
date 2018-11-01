import turtle
t = turtle.Turtle()

def countDown(n):
    if n <= 0:
        print("blastoff!")
    else:
        print(n)
        countDown(n-1)

def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result

def draw(t, length, n):
    t.speed(10)
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

turtle.mainloop()
