import math 

class Point:
    "Represents a point in two-dimensional geometric coordinates"

    def __init__(self, x=0, y=0):
        '''
        Initialize the position of a new point.
        The x and y coordinates can be spedified.
        If they are not, the point defaults to the origin.
        '''
        self.move(x, y)

    def move(self, x, y):
        '''
        Move the point to a new location in 2D space.
        '''
        self.x = x 
        self.y = y

    def reset(self):
        '''
        Reset the point back to the geometric origin: 0, 0
        '''
        self.move(0,0)

    def calculate_distance(self, other):
        '''
        Calculate the distance from this point to a second point
        passed as a parameter.
        '''
        dist = math.sqrt(
                (self.x - other.x)**2
                + (self.y - other.y)**2
                )
        return dist 

## Access Control 
class SecretString:
    "A not-at-all secure way to store a secret thing."

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrpyt(self, pass_phrase):
        '''
        Only show the string if the pass_phrase is correct.
        ''' 
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string 

        else:
            return ''

