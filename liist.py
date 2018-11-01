"""
-Lists are mutable

"""

numbers = [10, 20, 30, 40]

numbers[2] == 30

####
multi = [[1, 2, 3], ["a", "b", "c"]]

multi[1] == ["a", "b", "c"]

####
phrases = ["hello", "hey", "yo"]

####
empty = []

empty.append(3)

empty == [3]

####
[1,2,3,4,5] + [6,7,8,9,10]

[1,2,3,4,5,6,7,8,9,10]

[1, 2, 3] * 2
[1,2,3,1,2,3]

####
fruit = ["cherry", "banana", "pineapple", "updog", "pear"]

fruit[2:5] = ["pineapple", "updog", "pear"]

fruit[2:5][2:3][0][2] = "a"

####
def histogram(s):
    """
    takes string and makeas a histogram for num of times a letter appears in it

    s- string
    """
    d = dict()
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] = d[char] + 1
    return d

####
def nested_sum(t):
    total = 0
    for x in t:
        total += x
    return total

nesttest = [[10, 100, 1000], [600], [200, 300, 400]]

numbers

nested_sum(nesttest)
