def iterCountdown(n):
    while (n > 0):
        print(n)
        n = n - 1
    print("Blastoff! phshhhewww...")

"""
while True:
    n = input("Enter a number: ")
    if (n == "done"):
        break
    else:
        print(n)
"""

def iterFactorial(n):
    while (n >= 1):
        n = n * ((n-1)* n)
    print ("Non-factorial")

def reverse(string):
    for i in range(1, len(string)+1):
        print(string[- i])

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
