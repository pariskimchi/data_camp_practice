

import numpy as np

class Point:
    """ A point on 2D plane
    Attributes
    ----------
    x: float, default 0.0. the x coordinate of the point 
    y: float, default 0.0. the y coordinate of the point
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x 
        self.y = y

    def distance_to_origin(self):
        """calculate distance from the point 
        to origin(0,0)
        """
        return np.sqrt(self.x **2 + self.y **2)

    def reflect(self, axis):
        """Reflect the point with respect to x 
        or y axis
        """
        if axis == "x":
            self.y = -self.y
        elif axis == 'y':
            self.x = -self.x

        else:
            print("the argument axis only accept \
            value s'x' and 'y'!")