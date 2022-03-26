from line import Line

class Game: 
    def __init__(self) :
        self.players = ["player1" , "player2"]
    
    def play(self):
        firstLine = Line(0)
        firstLine.CreateSecretLine()