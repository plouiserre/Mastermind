import random
from piece import Piece, ColorCombinaison, PieceType

class Line : 
    def __init__(self, index, Log) :
        self.pieces = []
        self.index = index
        self.colors = [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, 
                        ColorCombinaison.PINK, ColorCombinaison.PURPLE, ColorCombinaison.RED,
                        ColorCombinaison.YELLOW]
        self.piecesValidation = []
        self.log = Log


    def FillSecretLine(self) :
        if self.index == 0 : 
            maxPiece = 4
            i = 0 
            while i < maxPiece :
                indexNewColor = random.randrange(0, len(self.colors))
                colorChoose = self.colors[indexNewColor]
                piece = Piece(i, colorChoose, PieceType.COLOR)
                self.colors.remove(colorChoose)
                self.pieces.append(piece)
                i += 1
            self.LogPiecesDefined("Secret Line")
        

    def GuessContent(self, colorsGuessing) :
        if self.index > 0 :
            maxPiece = 4
            i = 0
            while i < maxPiece :
                colorsToSelect = colorsGuessing[i]
                piece = Piece(i, None, PieceType.COLOR)
                piece.SetColor(colorsGuessing, self)
                colorsToSelect.remove(piece.Color)
                self.pieces.append(piece)
                i += 1
            self.LogPiecesDefined("Pieces Guessed")


    def LogPiecesDefined(self, labelLog) :
        self.log.LogInInfoLevel(labelLog)
        for piece in self.pieces : 
            self.log.LogInInfoLevel("Couleur :%s" % piece.Color)