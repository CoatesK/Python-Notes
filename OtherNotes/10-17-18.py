'''     Lists       '''
'''
Notes:

Strings are Sequences

Lists are sequences, but differ from strings.
        1. Lists can be a sequence of chars, numbers,
            string, lists, etc. ...
        2. Lists are MUTABLE
                a. (they CAN be changed)
        3. One can have nested lists
'''

def nested_sum(list1):
    total = 0
    for nested in t:
        total += sum(nested)
    return total

t = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
x = nested_sum(t)

def cumsum(list):
total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

y = cumsum(t)
