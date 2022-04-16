import random
from piece import Piece, ColorCombinaison, PieceType

class Line : 
    def __init__(self, index, Log) :
        self.pieces = []
        self.index = index
        self.colors = [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.CYAN, 
                        ColorCombinaison.PINK, ColorCombinaison.PURPLE, ColorCombinaison.RED,
                        ColorCombinaison.YELLOW]
        self.log = Log


    def fill_secret_line(self) :
        if self.index == 0 : 
            maxPiece = 4
            i = 0 
            while i < maxPiece :
                indexNewColor = random.randrange(0, len(self.colors))
                colorChoose = self.colors[indexNewColor]
                piece = Piece(i, colorChoose, PieceType.COLOR, self.log)
                self.colors.remove(colorChoose)
                self.pieces.append(piece)
                i += 1
            self.__log_pieces_defined("Secret Line")
        

    def guess_content(self, colorsGuessing) :
        if self.index > 0 :
            maxPiece = 4
            i = 0
            while i < maxPiece :
                colorsToSelect = colorsGuessing[i]
                piece = Piece(i, None, PieceType.COLOR, self.log)
                piece.set_color(colorsGuessing, self)
                self.__log_pieces_defined("colorsToSelect log %s" % colorsToSelect)
                self.__log_pieces_defined("couleur à supprimer %s" % piece.Color)
                colorsToSelect.remove(piece.Color)
                self.pieces.append(piece)
                i += 1
            self.__log_pieces_defined("Pieces Guessed")


    def __log_pieces_defined(self, labelLog) :
        self.log.Log_Info_Level(labelLog)
        for piece in self.pieces : 
            self.log.Log_Info_Level("Couleur :%s" % piece.Color)