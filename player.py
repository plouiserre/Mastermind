from line import Line
from enum import Enum

class PlayerType(Enum) :
    MASTER = 1
    GUESSER = 2

class Player :
    def __init__(self, playerType) :
        self.Type = playerType
        self.Winner = False

    def CreateSecretLine(self, grid) : 
        if self.Type == PlayerType.MASTER : 
            grid.CreateSecretLine(0)
        else :
            raise Exception("Only MASTER player can create SecretLine")

    def GuessSecretLine(self, index) :
        piecesGuessed = []
        if self.Type == PlayerType.GUESSER :
            LineProposed = Line(index)
            piecesGuessed = LineProposed.GuessLine()
        else : 
            raise Exception("Only GUESSER player can guess the secret Line")
        return piecesGuessed
    
