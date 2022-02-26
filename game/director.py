import pygame
from game.player import Player
from game.gem import Gem
from game.rock import Rock
from game.bigGem import BigGem

class Director:

    """
    Director class: Directs the gameplay and creates the pygame window

    Attributes:
        textFont - creates a pygame font object
        win - creates a pygame window
        run - Boolean to tell if the game is running
        score - tracks the player's score
        player - creates a Player object
        gem1, gem2 - creates Gem objects
        rock1, rock2, rock3 - creates Rock objects
    """


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

        self.bigGem = BigGem()

        self.rock1 = Rock()
        self.rock2 = Rock()
        self.rock3 = Rock()

    def playGame(self):
        """
        This function contains a while loop that updates the pygame window with gameplay changes. 
        """

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

            self.bigGem.update()

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
            
            self.bigGem.drawGem(self.win)

            self.player.drawPlayer(self.win)

            if pygame.Rect.colliderect(self.player.player_rect, self.gem1.gem_rect):
                self.gem1.__init__()
                self.score += 1
            if pygame.Rect.colliderect(self.player.player_rect, self.gem2.gem_rect):
                self.gem2.__init__()
                self.score += 1
            if pygame.Rect.colliderect(self.player.player_rect, self.bigGem.gem_rect):
                self.bigGem.__init__()
                self.score += 3
            if pygame.Rect.colliderect(self.player.player_rect, self.rock1.rock_rect):
                self.rock1.__init__()
                self.score -= 1
            if pygame.Rect.colliderect(self.player.player_rect, self.rock2.rock_rect):
                self.rock2.__init__()
                self.score -= 1
            if pygame.Rect.colliderect(self.player.player_rect, self.rock3.rock_rect):
                self.rock3.__init__()
                self.score -= 1
            
            scoreText = self.textFont.render("Score: {}".format(self.score), True, (255, 255, 255))
            
            self.win.blit(scoreText, (10, 10))

            # it refreshes the window
            pygame.display.update()