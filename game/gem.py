import random
import pygame
from game.color import Color
from game.velocity import Velocity

class Gem(Color):
    
    def __init__(self):

        super().__init__()

        self.x = random.randrange(10, 790, 10)
        self.y = random.randrange(0, 40)  

        self.velocity = Velocity()

        self.size = 10


    def drawGem(self, win):

        self.points = [(self.x - self.size, self.y), (self.x, self.y - self.size), (self.x + self.size, self.y), (self.x, self.y + self.size)]
        self.gem_rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
        pygame.draw.polygon(win, (self.r, self.g, self.b), self.points)

    def update(self):

        self.y += self.velocity.vel
        if self.y > 630:
            self.__init__()