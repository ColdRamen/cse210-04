import pygame
from game.keyboard import Keyboard

class Player(Keyboard):
    '''This class creates an instance of a player. The player is in the form of a rectangle.
        It inherits from the keyboard class. 
        
        Attributes:
        x(int) - creates an x coordinate.
        y(int) - creates a y coordinate.
        width(int) - The with of the player.
        height(int) - The height of the player.
        vel(int) - The speed of the player.
        win(int) - The window/display.
        player_rect - The shape of the player. '''

    def __init__(self):
        '''This function determines the coordinates of the player as well as its' size and speed.'''
        self.x = 400
        self.y = 550

        self.width = 20
        self.height = 20

        self.vel = 5
    
    def drawPlayer(self, win):
        '''This function draws the rectangular player onto the window.'''
        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 255, 255), self.player_rect)