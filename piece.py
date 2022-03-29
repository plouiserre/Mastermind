from enum import Enum


class ColorCombinaison(Enum) : 
    RED = 1
    PINK = 2
    GREEN = 3
    BLUE = 4
    YELLOW = 5
    PURPLE = 6
    ORANGE = 7

class ColorValidation(Enum) : 
    #RED color missing in the secret combinaison
    #YELLOR good color wrong place
    #WHITE same place same color 
    RED = 1
    YELLOW = 2
    WHITE = 3

class PieceType(Enum):
    COLOR = 1
    VALIDATION = 2

class Piece : 
    def __init__(self, index, color, type) :
        self.Index = index
        self.Type = type
        self.Color = color 