''' Tuples '''
'''
-associated with the type error
-Immutable
-You can change the tuples, but you can't just change the character...
        --You can't change characters, you have to change their values with
        the '+' operator.
-(Built in function): divmod(n, m)
        -- returns the quotient of the two entered numbers
            --'divmod(10, 5)' would return '(2,0)'
            --'divmod(6, 2)' would return '(3,0)'
        --you can assign variables to the outputted numbers of the divmod
            --'quot, rem = divmod(10,5)'
                - then type 'print(quot)'
                    -(this will output '2')
                -then type 'print(rem)'
                    -(this will output '0')
-Switching variables
        -- (This is the code itself as used in the terminal)...
            -- a = 5
            -- b = 6
            -- a,b = b,a
            -- print(a)
                - 6
            -- print(b)
                -5

Now for a few functions
'''

def printall(*args):
    print(args)

l = 'bobcat', 'I', 'really', 'dont', 'know'

printall(l)
