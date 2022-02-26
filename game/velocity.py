import random

class Velocity:
    '''This is an instance of velocity. The responsibility of this class is mainly to
       determine how fast the rocks and the gems fall from the top of the screen.

       Attributes:
       vel(int) - the speed at which gems and rocks fall down vertically.'''

    def __init__(self):
        '''generates random velocity for the gems and rocks'''
        self.vel = random.randrange(1, 5)