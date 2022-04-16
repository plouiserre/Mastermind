import random
from enum import Enum


class ColorCombinaison(Enum) : 
    RED = 1
    PINK = 2
    GREEN = 3
    BLUE = 4
    YELLOW = 5
    PURPLE = 6
    CYAN = 7

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
    def __init__(self, index, color, type, Log) :
        self.Index = index
        self.Type = type
        self.Color = color
        self.MaxPiece = 4
        self.log = Log
        self.CorrectColor = None


    def set_color(self, colorsGuessing, line) :
        colors = colorsGuessing[self.Index]
        colorIsChoosing = False 
        alert = 1
        while colorIsChoosing == False :
            if alert == 10 : 
                break
            self._choose_color_from_choice(colors)
            isColorPossible = True
            for piece in line.pieces :
                if piece.Color == self.Color :
                    isColorPossible = False 
            if isColorPossible :
                colorIsChoosing = True
                logmessage = "Color choose {0} for index {1}".format(self.Color, self.Index)
                self.log.Log_Info_Level(logmessage)
            alert += 1
    

    def _choose_color_from_choice(self, colors) :
        indexNewColor = random.randrange(0, len(colors))
        self.Color = colors[indexNewColor]


    def correct_piece(self, colorsSecretLine, colors) :
        correctColor = None
        if self.Color == colorsSecretLine[self.Index] : 
                correctColor = ColorValidation.WHITE
                self._manage_white_correction(colors)
        elif self.Color in colorsSecretLine : 
            correctColor = ColorValidation.YELLOW
            if self.Color in colors[self.Index] :
                colors[self.Index].remove(self.Color)
        else :
            correctColor = ColorValidation.RED
            j = 0
            while j < self.MaxPiece : 
                if self.Color in colors[j] :
                    colors[j].remove(self.Color)
                j += 1 
        self.CorrectColor = correctColor


    def _manage_white_correction(self, colors) :
        indexWhiteCorrection = 0
        while indexWhiteCorrection < self.MaxPiece :
            #second condition is needed because if you have a yellow correction before 
            #this white the algo has removed the color
            if indexWhiteCorrection != self.Index and self.Color in colors[indexWhiteCorrection]: 
                colors[indexWhiteCorrection].remove(self.Color)
            elif indexWhiteCorrection == self.Index: 
               for colorToInspect in colors[indexWhiteCorrection] :
                   if colorToInspect != self.Color : 
                       colors[indexWhiteCorrection].remove(colorToInspect)
            indexWhiteCorrection += 1