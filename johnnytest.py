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


letters = "mississippi"
foo = histogram(letters)
print(foo)
