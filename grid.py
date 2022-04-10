import random
import copy
from piece import ColorValidation, Piece, PieceType, ColorCombinaison
from line import Line

class Grid :
    def __init__(self, Log) :
        self.lines = []
        self.colors = { 0 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                1 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                2 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                3 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW]}
        self.log = Log

    def CreateSecretLine(self) :
        secretLine  = Line(0, self.log)
        if secretLine.index == 0 : 
            maxPiece = 4
            i = 0 
            while i < maxPiece :
                indexNewColor = random.randrange(0, len(secretLine.colors))
                colorChoose = secretLine.colors[indexNewColor]
                piece = Piece(i, colorChoose, PieceType.COLOR)
                secretLine.colors.remove(colorChoose)
                secretLine.pieces.append(piece)
                i += 1
            ''' To delete new loops'''
            self.log.LogInDebugLevel("Secret Line")
            for piece in secretLine.pieces : 
                self.log.LogInDebugLevel("Couleur :%s" % piece.Color)
        self.lines.append(secretLine)
        

    def GuessLine(self, index) : 
        colorsGuessing = copy.deepcopy(self.colors)
        
        guessLine = Line(index, self.log)

        guessLine.GuessContent(colorsGuessing)
        self.lines.append(guessLine)


    def CorrectLine(self, index) : 
        colorsSecretLine = []
        linesToCorrect = self.lines[index]
        secretLine = self.lines[0]
        correctColors = []
        
        for piece in secretLine.pieces : 
            colorsSecretLine.append(piece.Color)

        i = 0 
        maxPiece = 4
        while i < maxPiece :
            pieceToCorrect = linesToCorrect.pieces[i]
            correctColor = pieceToCorrect.CorrectPiece(colorsSecretLine, self.colors)
            correctColors.append(correctColor)
            i += 1

        allPiecesGuess = True
        for colorValidation in correctColors : 
            if colorValidation != ColorValidation.WHITE :
                allPiecesGuess = False
            
        self.piecesValidation = correctColors

        return allPiecesGuess