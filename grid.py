import random
import copy
from piece import ColorValidation, Piece, PieceType, ColorCombinaison
from line import Line

class Grid :
    def __init__(self, Log) :
        self.lines = []
        self.colors = { 0 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.CYAN, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                1 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.CYAN, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                2 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.CYAN, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                3 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.CYAN, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW]}
        self.log = Log
        self.Corrections = {}

    def create_secret_line(self) :
        secretLine  = Line(0, self.log)
        secretLine.fill_secret_line()
        self.lines.append(secretLine)
        

    def guess_line(self, index) : 
        colorsGuessing = copy.deepcopy(self.colors)
        
        guessLine = Line(index, self.log)

        guessLine.guess_content(colorsGuessing)
        self.lines.append(guessLine)


    def correct_line(self, index) : 
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
            pieceToCorrect.correct_piece(colorsSecretLine, self.colors)
            correctColors.append(pieceToCorrect.CorrectColor)
            i += 1

        allPiecesGuess = True
        for colorValidation in correctColors : 
            if colorValidation != ColorValidation.WHITE :
                allPiecesGuess = False
            
        self.Corrections[index] = correctColors

        return allPiecesGuess