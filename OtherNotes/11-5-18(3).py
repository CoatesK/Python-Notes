    '''"coords.py"'''

    '''
    This exception is raised when the number of coordinates does not match
    '''

    def __init__(self, message):
        self.message = message

class Point:

    '''
    Represents a point in n-space

    Attributes:
    point - tuple; the coordinates of the point as a tuple
    numCoords - int; the number of coordinates the tuple has
    '''

    def __init__(self, *args):
        self.numCoords = len(args)
        self.point = args

    def __str__(self):
        return str(self.point)

    def __add__(self, point):
        t = list()
        if self.numCoords != point.numCoords:
            raise


p = Point(2,3,4,5)
print(p)
print(type)
