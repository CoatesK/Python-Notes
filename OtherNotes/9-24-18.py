import math

def triangleArea(base, height):
    area = 0.5 * base * height
    return area

def isDivisibleByK(n, k):
    if n % k == 0:
        return True
    else:
        return False

x = isDivisibleByK(1.3, .5)
print(x)
