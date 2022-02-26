from game.gem import Gem

class BigGem(Gem):
    '''Creates an instance of a BigGem. When the player hits this gem, they earn 3 points!
    The class inherits some of the attributes of the  Gem class.

    Attributes:
    size(int) - This is the size of the BigGem.'''

    def __init__(self):
        '''This function initializes the size of the BigGem to 30.'''

        super().__init__()

        self.size = 30