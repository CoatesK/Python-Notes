x = 5
x += 1
'''
"+=" - synthetic sugar
'''

'''
Iteration:
    Repitition:
        - 1. for loop
        - 2. Recursion
        - 3. while loop (conditional iteration)
'''
def countdownRecursive(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

''''''

def countdownWhile(n):
    while(n > 0):
        print(n)
        n = n-1
    print("Blastoff!")

''''''

def printNumber():
    while True:
        w = input("Enter a word: ")
        u = input("Enter undesirable letters: ")
        

        '''
        if (n == "done"):
            break
        else:
            print(n)
        '''

def factorialWhile(i, n):
