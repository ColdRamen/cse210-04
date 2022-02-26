import pygame

class Keyboard:
    '''This is the keyboard class.
    Attributes:
    keys(string) - the keyboard left and right keys determine the direction of the player.'''

    def update(self, keys):
        '''This function uses the left and right keyboard keys to move the player and a specified velocity
        along the x-axis.'''
        if keys[pygame.K_LEFT] and self.x>0:
        
            # decrement in x co-ordinate
            self.x -= self.vel
        # if left arrow key is pressed
        if keys[pygame.K_RIGHT] and self.x<800-self.width:
            
            # increment in x co-ordinate
            self.x += self.vel