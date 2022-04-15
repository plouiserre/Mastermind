from grid import Grid
from render import Render

class Game: 
    def __init__(self, Log) :
        self.players = ["player1" , "player2"]
        self.log = Log
        self.maxTurn = 12
    
    def Play(self):
        grid = Grid(self.log)
        render = Render(grid)
        turn = 1 
        guesserWins = False
        grid.CreateSecretLine()
            
        while turn <= self.maxTurn and guesserWins == False:
            self.log.LogInInfoLevel("BEGIN Turn number  %s" % turn)
            grid.GuessLine(turn)
            #TODO pass by player like createsecretline and guesssecretline or delete player.py
            guesserWins = grid.CorrectLine(turn)
            turn += 1
            
        self.log.LogInInfoLevel("game finish")

        render.Rendering()
        
        if guesserWins == True :
            self.log.LogInInfoLevel("guesser wins")
        else :
            self.log.LogInInfoLevel("master winner")