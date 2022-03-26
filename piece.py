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
    RED = 1
    YELLOW = 2

class Piece : 
    def __init__(self, index, color) :
        self.Index = index
        self.Color = color