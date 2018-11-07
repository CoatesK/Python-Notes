def rows():
    print("+", '- ' * 4, "+", '- ' * 4, "+")

def column():
    print("|", '\t  ', "|", '\t     ', "|")

def grid():
    rows()
    column()
    column()
    column()
    column()
    rows()
    column()
    column()
    column()
    column()
    rows()

grid()
