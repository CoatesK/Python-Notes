class NumCoordsException(Exception):

class Point:
    """
    Representsa a point in nth spaceself.
    Attributes:
    point- tuple; the coordinates of the point as a tuple
    numCoords- int: the number of coordinates the tuple has
    """
    def __init__(self, *args):
        self.numCoords = len(args)
        self.point = args

    def __str__(self):
        return str(self.point)

    def __add__(self, point):
        t = list()
        if self.numCoords != point.numCoord
