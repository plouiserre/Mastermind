import random
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
                print("Index :",piece.Index, "Couleur :", piece.Color)
        self.lines.append(secretLine)

    #TODO factoriser with CreateSecretLine
    def GuessLine(self, index) : 
        #TODO à supprimer 
        print("index GuessLine", index)
        guessLine = Line(index)
        if guessLine.index > 0 :
            maxPiece = 4
            i = 0
            while i < maxPiece :
                indexNewColor = random.randrange(0, len(guessLine.colors))
                colorChoose = guessLine.colors[indexNewColor]
                piece = Piece(i, colorChoose, PieceType.COLOR)
                guessLine.colors.remove(colorChoose)
                guessLine.pieces.append(piece)
                i += 1
            #To Delete
            print("\n \nPieces Guessed \n")
            for piece in guessLine.pieces : 
                print("Index :",piece.Index, "Couleur :", piece.Color)
        self.lines.append(guessLine)
      
    def CorrectLine(self, index) : 
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
            piecesLinesToCorrect = linesToCorrect.pieces[i]
            piecesSecretLine = secretLine.pieces[i]
            if piecesLinesToCorrect.Color == piecesSecretLine.Color : 
                correctColors.append(ColorValidation.WHITE)
            elif piecesLinesToCorrect.Color in colorsSecretLine : 
                correctColors.append(ColorValidation.YELLOW)
            else :
                correctColors.append(ColorValidation.RED)
            i += 1

        #TODO to delete in finish phase
        allPiecesGuess = True
        for colorValidation in correctColors : 
            if colorValidation != ColorValidation.WHITE :
                allPiecesGuess = False
            print(colorValidation)

        self.piecesValidation = correctColors

        return allPiecesGuess
    