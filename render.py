from piece import ColorCombinaison 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Render :
    def __init__(self, Grid, MaxTurn) :
        self.grid = Grid
        self.maxTurn = MaxTurn


    def Rendering(self) :
        i = 0
        while i <= self.maxTurn :
            labelLine =  None 
            if i == 0 :
                labelLine = "S" 
            else :
                labelLine = i 
            if i == 0 : # à supprimer juste après
                contentLine = self.RenderSpecificLine(i)
                print(" ------------- ")
                print("|{}{}".format(labelLine, contentLine))
                print(" ------------- ")
            i += 1

        


    def RenderSpecificLine(self, numberLine) :
        contentLine = ""

        line = self.grid.lines[numberLine]
        for piece in line.pieces :
            contentLine += self.RenderSpecificPiece(piece)

        return contentLine


    
    def RenderSpecificPiece(self, piece) :
        if piece.Color == ColorCombinaison.PINK :
            return "|"+bcolors.HEADER+"█"+bcolors.ENDC+"|"
        elif piece.Color == ColorCombinaison.BLUE : 
            return "|"+bcolors.OKBLUE+"█"+bcolors.ENDC+"|"
        elif piece.Color == ColorCombinaison.CYAN : 
            return "|"+bcolors.OKCYAN+"█"+bcolors.ENDC+"|"
        elif piece.Color == ColorCombinaison.GREEN : 
            return "|"+bcolors.OKGREEN+"█"+bcolors.ENDC+"|"
        elif piece.Color == ColorCombinaison.YELLOW : 
            return "|"+bcolors.WARNING+"█"+bcolors.ENDC+"|"
        #TODO ca correspond à purple mais c'est peut être trop proche du red à retravailler
        else : 
            return "|"+bcolors.FAIL+"█"+bcolors.ENDC+"|"