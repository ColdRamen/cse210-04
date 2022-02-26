import pygame

class Keyboard:

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x>0:
        
            # decrement in x co-ordinate
            self.x -= self.vel
        # if left arrow key is pressed
        if keys[pygame.K_RIGHT] and self.x<800-self.width:
            
            # increment in x co-ordinate
            self.x += self.vel