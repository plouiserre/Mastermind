from grid import Grid

class Game: 
    def __init__(self, Log) :
        self.players = ["player1" , "player2"]
        self.log = Log
    
    def Play(self):
        grid = Grid(self.log)
        turn = 1 
        guesserWins = False
        grid.CreateSecretLine()
            
        while turn <= 12 and guesserWins == False:
            self.log.LogInDebugLevel("BEGIN Turn number  %s" % turn)
            grid.GuessLine(turn)
            #TODO pass by player like createsecretline and guesssecretline or delete player.py
            guesserWins = grid.CorrectLine(turn)
            turn += 1
            
        self.log.LogInDebugLevel("game finish")
        if guesserWins == True :
            self.log.LogInDebugLevel("guesser wins")
        else :
            self.log.LogInDebugLevel("master winner")