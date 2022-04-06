import random
import copy
import operator
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
                colorChoose = self.ChooseColorFromChoice(secretLine.colors)                
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
        '''
        if guessLine.index > 0 :
            maxPiece = 4
            i = 0
            while i < maxPiece :
                colorsToSelect = colorsGuessing[i]
                colorChoose = self.ChooseColorGuessing(colorsGuessing, i, guessLine.pieces)
                piece = Piece(index, colorChoose, PieceType.COLOR)
                colorsToSelect.remove(colorChoose)
                guessLine.pieces.append(piece)
                i += 1
            #TODO To Delete
            print("\n \nPieces Guessed \n")
            for piece in guessLine.pieces : 
                print("Couleur :", piece.Color)
        '''
        guessLine.GuessContent(colorsGuessing)
        self.lines.append(guessLine)


    #TODO method to optimize
    def ChooseColorGuessing(self, colorsGuessing, index, pieces) :
        colors = colorsGuessing[index]
        colorIsChoosing = False 
        alert = 1
        while colorIsChoosing == False :
            if alert == 10 : 
                colorChoose = self.ChooseColorFromChoice(colors)
                break
            colorChoose = self.ChooseColorFromChoice(colors)
            isColorPossible = True
            for piece in pieces :
                if piece.Color == colorChoose :
                    isColorPossible = False 
            if isColorPossible :
                colorIsChoosing = True
            alert += 1
        return colorChoose

      
    def CorrectLine(self, index) : 
        colorsLineGuess = []
        colorsSecretLine = []
        linesToCorrect = self.lines[index]
        secretLine = self.lines[0]
        correctColors = []
        
        for piece in linesToCorrect.pieces : 
            colorsLineGuess.append(piece.Color)
        for piece in secretLine.pieces : 
            colorsSecretLine.append(piece.Color)

        i = 0 
        maxPiece = 4
        while i < maxPiece :
            pieceToCorrect = linesToCorrect.pieces[i]
            pieceSecret = secretLine.pieces[i]
            if pieceToCorrect.Color == pieceSecret.Color : 
                correctColors.append(ColorValidation.WHITE)
                self.ManageWhiteCorrection(maxPiece, self.colors, i, pieceToCorrect.Color)
            elif pieceToCorrect.Color in colorsSecretLine : 
                correctColors.append(ColorValidation.YELLOW)
                self.colors[i].remove(pieceToCorrect.Color)
            else :
                correctColors.append(ColorValidation.RED)
                j = 0
                while j < maxPiece : 
                    if pieceToCorrect.Color in self.colors[j] :
                        self.colors[j].remove(pieceToCorrect.Color)
                    j += 1 
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

    #TODO to delete because after it will be useless
    def ChooseColorFromChoice(self, colors) :
        indexNewColor = random.randrange(0, len(colors))
        colorChoose = colors[indexNewColor]
        return colorChoose