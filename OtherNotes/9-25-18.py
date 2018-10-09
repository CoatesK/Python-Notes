def factorial(n):

    '''
    Description:
    "The Factorial Sequence"
    This function finds the factorial of entered # 'n' and then finds
    the factorials of those below it as well.

    Parameters:
    n = number that is the first factorial output.

    Return Values:

    '''

    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

x = factorial(900)

def fibonacci(n):
    '''
    "Fibonacci Sequence"
    '''
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

y = fibonacci(20)
print(y)
