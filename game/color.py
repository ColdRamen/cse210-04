import random

class Color: 
    '''Creates an instance of Color. The gems and rocks randomly have different colors.
    Attributes:
    (r, g, b) - The rgb color values to be assigned to the falling gems and rocks.'''

    def __init__(self):
        '''This function randomly generates rgb values to the gems and rocks.'''

        self.r = random.randrange(40, 255)
        self.g = random.randrange(40, 255)
        self.b = random.randrange(40, 255)