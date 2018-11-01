def trichotomy(n):
    '''
    Description: states wether an integer is positive,
    negative, or zero

    Parameters:
    n - numeric value (int, float) the number checked

    Return values: None
    '''
    if n > 0:
        print(n, "is positive")
    elif n < 0:
        prin ("n is negative")
    else:
        print("n is zero")

def checkSingleDigit(n):
    '''
    Description: check to see if "n" is a single
    digit integer

    parameter: n - int; the integer to be checked

    Return Values: None
    '''

    if n < 10 and n < 10:
        print(n, " is a single digit number")
    else:
        print(n, " is not a single digit number")


if __name__== '__main__':
    string = input("Welcome back Captain. Please enter your Code Number: ")
    checkSingleDigit(int(string))
