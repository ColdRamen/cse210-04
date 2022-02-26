import random
import pygame
from game.color import Color
from game.velocity import Velocity

class Gem(Color):
    '''Creates an instance of a Gem. This class inherits the attributes from the Color class.
       
       ATTRIBUTES:
       radius(int) - Chosen randomly from numbers between 20-30. This determine the size of the rocks.
       x(int) - The x-coordinate
       y(int) - The y-coordinate
       velocity(int) - The speed at which gems fall.
       size (int) - The physical size of the gem.
       points(int) - gets the coordinates of the gem.
       gem_rect (int) - creates the rectangular border of the gem. '''
    
    def __init__(self):
        '''This function randomly places a gem on the screen. It imports the the velocity function.
        and determines the size of the rocks.'''
        super().__init__()

        self.x = random.randrange(10, 790, 10)
        self.y = random.randrange(0, 40)  

        self.velocity = Velocity()

        self.size = 10


    def drawGem(self, win):
        '''This function draws the gems onto the screen using the specified coordinates.'''

        self.points = [(self.x - self.size, self.y), (self.x, self.y - self.size), (self.x + self.size, self.y), (self.x, self.y + self.size)]
        self.gem_rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
        pygame.draw.polygon(win, (self.r, self.g, self.b), self.points)

    def update(self):
        '''This function continuously updates the velocity of the gems.'''
        self.y += self.velocity.vel
        if self.y > 630:
            self.__init__()