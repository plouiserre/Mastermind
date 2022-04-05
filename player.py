from line import Line
from enum import Enum

#TODO changer enum cf https://fr.wikipedia.org/wiki/Mastermind
class PlayerType(Enum) :
    MASTER = 1
    GUESSER = 2

class Player :
    def __init__(self, playerType) :
        self.Type = playerType
        self.Winner = False

    def CreateSecretLine(self, grid) : 
        if self.Type == PlayerType.MASTER : 
            grid.CreateSecretLine()
        else :
            raise Exception("Only MASTER player can create SecretLine")

    def GuessSecretLine(self, grid, index, colors) :
        if self.Type == PlayerType.GUESSER :
            grid.GuessLine(index, colors)
        else : 
            raise Exception("Only GUESSER player can guess the secret Line")
        
