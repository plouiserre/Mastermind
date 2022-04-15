from piece import ColorCombinaison, ColorValidation 

class bcolors:
    WHITE = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    PURPLE  = '\033[35m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Render :
    def __init__(self, Grid) :
        self.grid = Grid


    def Rendering(self) :
        i = 0
        maxTurn = len(self.grid.lines)
        while i < maxTurn :
            labelLine =  None 
            if i == 0 :
                labelLine = "S" 
            else :
                labelLine = i 
            contentLine = self.RenderSpecificLine(i)
            print(" ----------------- ")
            print("|{}|{}".format(labelLine, contentLine))
            print(" ----------------- ")
            i += 1

        


    def RenderSpecificLine(self, numberLine) :
        contentLine = ""

        line = self.grid.lines[numberLine]
        if numberLine > 0 : 
            for piece in line.pieces :
                contentLine += self.RenderCorrection(piece)
        else :
            contentLine +="    "

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
        elif piece.Color == ColorCombinaison.PURPLE : 
            return "|"+bcolors.PURPLE+"█"+bcolors.ENDC+"|"
        else : 
            return "|"+bcolors.FAIL+"█"+bcolors.ENDC+"|"


    def RenderCorrection(self, piece) :
        if piece.CorrectColor == ColorValidation.RED :
            return bcolors.FAIL+"¤"+bcolors.ENDC
        elif piece.CorrectColor == ColorValidation.YELLOW : 
            return bcolors.WARNING+"¤"+bcolors.ENDC
        else :
            return bcolors.WHITE+"¤"+bcolors.ENDC