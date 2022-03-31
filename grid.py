import random
import copy
from piece import ColorValidation, Piece, ColorCombinaison, PieceType
from line import Line

class Grid :
    def __init__(self) :
        self.lines = []

    #TODO factoriser with GuessLine
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
        

    #TODO factoriser with CreateSecretLine
    def GuessLine(self, index, colors) : 
        colorsGuessing = copy.deepcopy(colors)
        
        guessLine = Line(index)

        if guessLine.index > 0 :
            maxPiece = 4
            i = 0
            while i < maxPiece :
                #TODO delete next print
                colorsToSelect = colorsGuessing[i]
                indexNewColor = random.randrange(0, len(colorsToSelect))
                colorChoose = colorsToSelect[indexNewColor]
                piece = Piece(index, colorChoose, PieceType.COLOR)
                colorsToSelect.remove(colorChoose)
                guessLine.pieces.append(piece)
                i += 1
            #TODO To Delete
            print("\n \nPieces Guessed \n")
            for piece in guessLine.pieces : 
                print("Couleur :", piece.Color)
        self.lines.append(guessLine)
        
      
    def CorrectLine(self, index, colors) : 
        colorsLineGuess = []
        colorsSecretLine = []
        linesToCorrect = self.lines[index]
        secretLine = self.lines[0]
        correctColors = []
        
        #TODO à factoriser et optimiser
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
            elif pieceToCorrect.Color in colorsSecretLine : 
                correctColors.append(ColorValidation.YELLOW)
                colors[i].remove(pieceToCorrect.Color)
            else :
                correctColors.append(ColorValidation.RED)
                j = 0
                while j < maxPiece : 
                    colors[j].remove(pieceToCorrect.Color)
                    j += 1 

            i += 1

        allPiecesGuess = True
        for colorValidation in correctColors : 
            if colorValidation != ColorValidation.WHITE :
                allPiecesGuess = False
            
        self.piecesValidation = correctColors

        return allPiecesGuess
    