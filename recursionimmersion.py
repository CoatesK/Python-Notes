def factorial(n):
    """
    Description: Gives the value of a given number in it's factorial state

    Parameters: n - given integer, to be comupted for it's factorial

    Return Values: the factorial of n
    """
    if n == 1:
        return 1
    return n * 900 *factorial(n-1)

def fibonacci(n):
    """
    Description: Shows the nth term of the fibonacci sequence

    Parameters: n - the iteration number of the fibonacci sequence being found

    Return Values: the term from the sequence
    """
    if n <= 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def pell(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    2*P*(n-1)+2*P*(n-2)

def countdown(n):
    if n == 0:
        return 0
    else:
        print (n)
        countdown(n-1)

def restring(s, n):
    if n <= 1:
        print(s)
    else:
        print (s)
        restring("bro", n - 1)

def 

answer = restring("bro", 10)

print(answer)
