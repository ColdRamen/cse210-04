from game.gem import Gem
import random
import pygame

class Rock(Gem):
    '''Creates an instance of a rock. This class inherits some attributes from the gem class.
       
       ATTRIBUTES:
       radius(int) - Chosen randomly from numbers between 20-30. This determine the size of the rocks.'''

    def __init__(self):
        '''This function randomly generates rocks of different radii.'''

        super().__init__()

        self.radius = random.randrange(20, 60)

    def drawRock(self, win):
        '''This function draws the coordinates of the rock on the display.'''

        self.rock_rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        pygame.draw.ellipse(win, (90, 100, 110), self.rock_rect)
