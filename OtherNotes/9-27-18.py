def printText(s, n):
    if n <= 1:
        print(s)
    else:
        print(s)
        printText(s, n-1)

def countdown(n):
    if n <= 0:
        print(n)
    else:
        print(n)
        countdown(n-1)

def exponentOut(x, n):
    if n == 0:
        print(1)
    else:
        print(x**n)
        exponentOut(x, n-1)
