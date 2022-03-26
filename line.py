import random
from piece import Piece, ColorCombinaison

class Line : 
    def __init__(self, index) :
        self.pieces = []
        self.index = index

    def CreateSecretLine(self) :
        if self.index == 0 : 
            colors = [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, 
                        ColorCombinaison.PINK, ColorCombinaison.PURPLE, ColorCombinaison.RED,
                        ColorCombinaison.YELLOW]
            maxPiece = 4
            i = 0 
            while i < maxPiece :
                indexNewColor = random.randrange(0, len(colors))
                colorChoose = colors[indexNewColor]
                piece = Piece(i, colorChoose)
                colors.remove(colorChoose)
                self.pieces.append(piece)
                i += 1
            ''' To delete new loops'''
            for piece in self.pieces : 
                print("Index :",piece.Index, "Couleur :", piece.Color)