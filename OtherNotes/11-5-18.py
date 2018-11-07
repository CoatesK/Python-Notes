class Kangaroo():
    ''' a Kangaroo is a marsupial'''

    def __init__(self, name, contents = []):
        self.name = name
        '''initializes the pouch contents to be the empty list'''
        if contents == None:
            self.contents = []
        else:
            self.contents = contents

    def __str__(self):
        t = [self.name + ' has pouch contents: ']
        for obj in self.contents:
            s = '   ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        self.contents.append(item)
