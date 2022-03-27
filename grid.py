import random
from piece import Piece, ColorCombinaison
from line import Line

class Grid :
    def CreateSecretLine(self) :
        secretLine  = Line(0)
        if secretLine.index == 0 : 
            maxPiece = 4
            i = 0 
            while i < maxPiece :
                indexNewColor = random.randrange(0, len(secretLine.colors))
                colorChoose = secretLine.colors[indexNewColor]
                piece = Piece(i, colorChoose)
                secretLine.colors.remove(colorChoose)
                secretLine.pieces.append(piece)
                i += 1
            ''' To delete new loops'''
            print("Secret Line \n")
            for piece in secretLine.pieces : 
                print("Index :",piece.Index, "Couleur :", piece.Color)
        return secretLine

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