# import sys
# import random
from tkinter import Tk, Frame, Canvas, ALL, NW

class Board(Canvas):
    """
    Creates the game board with Tkinter.
    """

    def __init__(self):
        super().__init__(width=800, height=600, background="black")

        self.initGame()
        self.pack()

    def initGame(self):

        # Holds the value of the player's score
        self.score = 0

        # How fast the player moves left and right
        self.moveX = 10

        # This is the player's starting position
        self.playerX = 395
        self.playerY = 560

        self.createObjects()
        self.bind_all("<Key>", self.onKeyPressed)

    def createObjects(self):

        self.create_text(30, 10, text="Score: {0}".format(self.score), font=('16'), tag="score", fill="white")

        # Creates the symbol representing the player, with the tag "player"
        self.create_text(self.playerX, self.playerY, text="#", font=('30'), tag="player", fill="white")

    def onKeyPressed(self, e):
        
        key = e.keysym

        # Gets the player text object
        player = self.find_withtag("player")

        # Gets the player's coordinates
        player_coords = self.coords("player")
        playerX = player_coords[0]

        # Checks whether the left or right arrow is being pressed and moves the player accordingly
        LEFT_CURSOR_KEY = "Left"
        if key == LEFT_CURSOR_KEY and playerX >= 10:

            self.move(player, -self.moveX, 0)

        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY and playerX <= 790:

            self.move(player, self.moveX, 0)



class Greed(Frame):
    """
    Creates an instance of Board() and creates the game window.
    """

    def __init__(self):

        super().__init__()

        self.master.title("Greed")
        self.board = Board()
        self.pack()

if __name__ == "__main__":

    root = Tk()
    nib = Greed()
    root.mainloop()
