import random
import copy
import operator
from piece import ColorValidation, Piece, ColorCombinaison, PieceType
from line import Line

class Grid :
    def __init__(self) :
        self.lines = []

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
        

    def GuessLine(self, index, colors) : 
        colorsGuessing = copy.deepcopy(colors)
        
        self.OrderColors(colorsGuessing)
        
        guessLine = Line(index)

        if guessLine.index > 0 :
            maxPiece = 4
            i = 0
            while i < maxPiece :
                colorsToSelect = colorsGuessing[i]
                colorChoose = self.ChooseColorGuessing(colorsToSelect, guessLine.pieces)
                piece = Piece(index, colorChoose, PieceType.COLOR)
                colorsToSelect.remove(colorChoose)
                guessLine.pieces.append(piece)
                i += 1
            #TODO To Delete
            print("\n \nPieces Guessed \n")
            for piece in guessLine.pieces : 
                print("Couleur :", piece.Color)
        self.lines.append(guessLine)


    def OrderColors(self, colors) :
        print(colors)
        LinesByOccurences = {}
        for key, values in colors.items() :
            occurences = len(values)
            LinesByOccurences[key] = occurences
        
        OccurencesSortend = sorted(LinesByOccurences.items(), key=operator.itemgetter(1))
        keysSorted = []
        for sort in OccurencesSortend : 
            keysSorted.append(sort[0])

        ColorsSorted = {}
        for key in keysSorted : 
            ColorsSorted[key] = colors[key]

        colors = ColorsSorted
        print("colors after ordercolors", colors)
        

    #TODO method to optimize
    def ChooseColorGuessing(self, colors, pieces) :
        colorIsChoosing = False 
        colorChoose = None
        alert = 1
        while colorIsChoosing == False :
            if alert == 10 : 
                print("problem with ", colorChoose,"and ",colors)
            indexNewColor = random.randrange(0, len(colors))
            colorChoose = colors[indexNewColor]
            isColorPossible = True
            for piece in pieces :
                if piece.Color == colorChoose :
                    isColorPossible = False 
            if isColorPossible :
                colorIsChoosing = True
            alert += 1
        return colorChoose

      
    def CorrectLine(self, index, colors) : 
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
                self.ManageWhiteCorrection(maxPiece, colors, i, pieceToCorrect.Color)
            elif pieceToCorrect.Color in colorsSecretLine : 
                correctColors.append(ColorValidation.YELLOW)
                colors[i].remove(pieceToCorrect.Color)
                #TODO to delete when everything will be working
                print("Correction jaune de la couleur", pieceToCorrect.Color,". Je la supprime de la ligne ",i)
            else :
                correctColors.append(ColorValidation.RED)
                j = 0
                while j < maxPiece : 
                    if pieceToCorrect.Color in colors[j] :
                        colors[j].remove(pieceToCorrect.Color)
                    j += 1 
                print("Correction rouge de la couleur",pieceToCorrect.Color,". Je la supprime partout")
            i += 1

        allPiecesGuess = True
        for colorValidation in correctColors : 
            if colorValidation != ColorValidation.WHITE :
                allPiecesGuess = False
            
        self.piecesValidation = correctColors

        return allPiecesGuess

    
    #TODO delete print in this method
    def ManageWhiteCorrection(self, maxPiece, colors, index, color) :
        indexWhiteCorrection = 0
        print("Correction blanche \n")
        while indexWhiteCorrection < maxPiece :
            #second condition is needed because if you have a yellow correction before 
            #this white the algo has removed the color
            if indexWhiteCorrection != index and color in colors[indexWhiteCorrection]: 
                colors[indexWhiteCorrection].remove(color)
                print("Suppression de ",color,"à la ligne ",indexWhiteCorrection)
            elif indexWhiteCorrection == index: 
               #faire une boucle sur les couleurs et supprimer si c'est pas color 
               for colorToInspect in colors[indexWhiteCorrection] :
                   if colorToInspect != color : 
                       colors[indexWhiteCorrection].remove(colorToInspect)
                       print("Suppressoin de ",colorToInspect,"dans l'index",indexWhiteCorrection)
            indexWhiteCorrection += 1