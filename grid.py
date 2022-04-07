import random
import copy
from piece import ColorValidation, Piece, PieceType, ColorCombinaison
from line import Line

class Grid :
    def __init__(self) :
        self.lines = []
        self.colors = { 0 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                1 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                2 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                3 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW]}

    def CreateSecretLine(self) :
        secretLine  = Line(0)
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
            print("Secret Line \n")
            for piece in secretLine.pieces : 
                print("Couleur :", piece.Color)
        self.lines.append(secretLine)
        

    def GuessLine(self, index) : 
        colorsGuessing = copy.deepcopy(self.colors)
        
        guessLine = Line(index)

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

    
    def ManageWhiteCorrection(self, maxPiece, colors, index, color) :
        indexWhiteCorrection = 0
        while indexWhiteCorrection < maxPiece :
            #second condition is needed because if you have a yellow correction before 
            #this white the algo has removed the color
            if indexWhiteCorrection != index and color in colors[indexWhiteCorrection]: 
                colors[indexWhiteCorrection].remove(color)
            elif indexWhiteCorrection == index: 
               for colorToInspect in colors[indexWhiteCorrection] :
                   if colorToInspect != color : 
                       colors[indexWhiteCorrection].remove(colorToInspect)
            indexWhiteCorrection += 1