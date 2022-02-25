import pygame
import random

class Director:

    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.textFont = pygame.font.SysFont('Ubuntu', 20)
 
        # Figure out text in pygame

        self.win = pygame.display.set_mode((800, 600))
  
        pygame.display.set_caption("Greed")
        
        self.run = True
        self.score = 0

        self.player = Player()

        self.gem1 = Gem()
        self.gem2 = Gem()

        self.rock1 = Rock()
        self.rock2 = Rock()
        self.rock3 = Rock()
        


    def playGame(self):
        while self.run:
    # creates time delay of 10ms 
            pygame.time.delay(10)
            
            # iterate over the list of Event objects  
            # that was returned by pygame.event.get() method.  
            for event in pygame.event.get():
                
                # if event object type is QUIT  
                # then quitting the pygame  
                # and program both.  
                if event.type == pygame.QUIT:
                    
                    # it will make exit the while loop 
                    self.run = False
            # stores keys pressed 
            

            keys = pygame.key.get_pressed()
            self.player.update(keys)

            self.gem1.update()
            self.gem2.update()

            self.rock1.update()
            self.rock2.update()
            self.rock3.update()

            
            

            # completely fill the surface object  
            # with black colour  
            self.win.fill((0, 0, 0))
            
            # drawing object on screen which is rectangle here 
            self.rock1.drawRock(self.win)
            self.rock2.drawRock(self.win)
            self.rock3.drawRock(self.win)

            self.gem1.drawGem(self.win)
            self.gem2.drawGem(self.win)
            
            self.player.drawPlayer(self.win)

            if pygame.Rect.colliderect(self.player.player_rect, self.gem1.gem_rect):
                self.gem1.__init__()
                self.score += 1
            if pygame.Rect.colliderect(self.player.player_rect, self.gem2.gem_rect):
                self.gem2.__init__()
                self.score += 1
            if pygame.Rect.colliderect(self.player.player_rect, self.rock1.rock_rect):
                self.rock1.__init__()
                self.score -= 1
            if pygame.Rect.colliderect(self.player.player_rect, self.rock2.rock_rect):
                self.rock2.__init__()
                self.score -= 1
            if pygame.Rect.colliderect(self.player.player_rect, self.rock3.rock_rect):
                self.rock3.__init__()
                self.score -= 1
            
            # it refreshes the window
            pygame.display.update()
        
class Player:

    def __init__(self):

        self.x = 400
        self.y = 550

        self.width = 20
        self.height = 20

        self.vel = 5
    
    def drawPlayer(self, win):
        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 255, 255), self.player_rect)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x>0:
                
            # decrement in x co-ordinate
            self.x -= self.vel
        # if left arrow key is pressed
        if keys[pygame.K_RIGHT] and self.x<800-self.width:
            
            # increment in x co-ordinate
            self.x += self.vel

# Add Object Class
# Gem and Rock will inherit

class Gem:
    
    def __init__(self):

        self.x = random.randrange(10, 790, 10)
        self.y = random.randrange(0, 40)

        self.vel = random.randrange(2, 4)

        self.r = random.randrange(40, 255)
        self.g = random.randrange(40, 255)
        self.b = random.randrange(40, 255)

        

    def drawGem(self, win):

        self.points = [(self.x - 10, self.y), (self.x, self.y - 10), (self.x + 10, self.y), (self.x, self.y + 10)]
        self.gem_rect = pygame.Rect(self.x - 10, self.y - 10, 20, 20)
        pygame.draw.polygon(win, (self.r, self.g, self.b), self.points)

    def update(self):

        self.y += self.vel
        if self.y > 630:
            self.__init__()

class Rock:

    def __init__(self):

        self.x = random.randrange(10, 790, 10)
        self.y = random.randrange(-10, 30)

        self.radius = random.randrange(20, 30)

        self.vel = random.randrange(2, 4)

        

    def drawRock(self, win):
        self.rock_rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        pygame.draw.ellipse(win, (90, 100, 110), self.rock_rect)

    def update(self):

        self.y += self.vel
        if self.y > 630:
            self.__init__()


if __name__ == "__main__":

    director = Director()
    director.playGame()