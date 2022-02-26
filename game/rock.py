from game.gem import Gem
import random
import pygame

class Rock(Gem):

    def __init__(self):

        super().__init__()

        self.radius = random.randrange(20, 30)

    def drawRock(self, win):

        self.rock_rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        pygame.draw.ellipse(win, (90, 100, 110), self.rock_rect)
