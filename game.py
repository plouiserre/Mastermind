from grid import Grid
from render import Render

class Game: 
    def __init__(self, Log) :
        self.players = ["player1" , "player2"]
        self.log = Log
        self.maxTurn = 12
    
    def play(self):
        grid = Grid(self.log)
        render = Render(grid)
        turn = 1 
        guesserWins = False
        grid.create_secret_line()
            
        while turn <= self.maxTurn and guesserWins == False:
            self.log.Log_Info_Level("BEGIN Turn number  %s" % turn)
            grid.guess_line(turn)
            #TODO pass by player like createsecretline and guesssecretline or delete player.py
            guesserWins = grid.correct_line(turn)
            turn += 1
            
        self.log.Log_Info_Level("game finish")

        render.rendering()
        
        if guesserWins == True :
            self.log.Log_Info_Level("guesser wins")
        else :
            self.log.Log_Info_Level("master winner")