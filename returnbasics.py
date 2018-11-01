import math

def triarea(b, h):
    area = b * h * (1 / 2)
    return area

def divisibleByN(n, x):
    if x % n == 0:
        return True
    else:
        return False

def pythag(x, y, z, n):
    if (x**n) * (y**n) == (z**n):
        return true
    else:
        return false
