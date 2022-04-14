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
            print(" ---------------------------------- ")
            print("|%s                                 |" % labelLine)
            print(" ---------------------------------- ")
            i += 1
        