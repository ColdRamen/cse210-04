import pygame
from game.keyboard import Keyboard

class Player(Keyboard):

    def __init__(self):

        self.x = 400
        self.y = 550

        self.width = 20
        self.height = 20

        self.vel = 5
    
    def drawPlayer(self, win):
        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 255, 255), self.player_rect)