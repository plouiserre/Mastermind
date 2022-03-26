import random
from piece import Piece, ColorCombinaison

class Line : 
    def __init__(self, index) :
        self.pieces = []
        self.index = index
        self.colors = [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, 
                        ColorCombinaison.PINK, ColorCombinaison.PURPLE, ColorCombinaison.RED,
                        ColorCombinaison.YELLOW]

    def CreateSecretLine(self) :
        if self.index == 0 : 
            maxPiece = 4
            i = 0 
            while i < maxPiece :
                indexNewColor = random.randrange(0, len(self.colors))
                colorChoose = self.colors[indexNewColor]
                piece = Piece(i, colorChoose)
                self.colors.remove(colorChoose)
                self.pieces.append(piece)
                i += 1
            ''' To delete new loops'''
            print("Secret Line \n")
            for piece in self.pieces : 
                print("Index :",piece.Index, "Couleur :", piece.Color)

    #for the moment I don't factorize GuessLine with CreateSecretLine because the code will change in the future
    def GuessLine(self) : 
        piecesGuessed = []
        if self.index > 0 :
            maxPiece = 4
            i = 0
            while i < maxPiece :
                indexNewColor = random.randrange(0, len(self.colors))
                colorChoose = self.colors[indexNewColor]
                piece = Piece(i, colorChoose)
                self.colors.remove(colorChoose)
                piecesGuessed.append(piece)
                i += 1
            print("Pieces Guessed \n")
            for piece in piecesGuessed : 
                print("Index :",piece.Index, "Couleur :", piece.Color)
        return piecesGuessed

