import random
from piece import Piece, ColorCombinaison, PieceType

class Line : 
    def __init__(self, index) :
        self.pieces = []
        self.index = index
        self.colors = [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, 
                        ColorCombinaison.PINK, ColorCombinaison.PURPLE, ColorCombinaison.RED,
                        ColorCombinaison.YELLOW]
        self.piecesValidation = []
        

    def GuessContent(self, colorsGuessing) :
        if self.index > 0 :
            maxPiece = 4
            i = 0
            while i < maxPiece :
                colorsToSelect = colorsGuessing[i]
                colorChoose = self.ChooseColor(colorsGuessing, i)
                piece = Piece(self.index, colorChoose, PieceType.COLOR)
                colorsToSelect.remove(colorChoose)
                self.pieces.append(piece)
                i += 1
            #TODO To Delete
            print("\n \nPieces Guessed \n")
            for piece in self.pieces : 
                print("Couleur :", piece.Color)


    #TODO trouver un autre nom
    def ChooseColor(self, colorsGuessing, index) :
        colors = colorsGuessing[index]
        colorIsChoosing = False 
        alert = 1
        while colorIsChoosing == False :
            if alert == 10 : 
                colorChoose = self.ChooseColorFromChoice(colors)
                break
            colorChoose = self.ChooseColorFromChoice(colors)
            isColorPossible = True
            for piece in self.pieces :
                if piece.Color == colorChoose :
                    isColorPossible = False 
            if isColorPossible :
                colorIsChoosing = True
            alert += 1
        return colorChoose


    def ChooseColorFromChoice(self, colors) :
        indexNewColor = random.randrange(0, len(colors))
        colorChoose = colors[indexNewColor]
        return colorChoose