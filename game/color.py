import random

class Color: 

    def __init__(self):

        self.r = random.randrange(40, 255)
        self.g = random.randrange(40, 255)
        self.b = random.randrange(40, 255)