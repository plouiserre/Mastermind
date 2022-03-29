from line import Line
#TODO : à supprimer
from player import PlayerType, Player
from grid import Grid

#TODO : change class name to board
class Game: 
    def __init__(self) :
        self.players = ["player1" , "player2"]
    
    #TODO : manage all game
    def Play(self):
        grid = Grid()
        Master = Player(PlayerType.MASTER)
        Guesser = Player(PlayerType.GUESSER)
        turn = 1 
        guesserWins = False
        
        while turn <= 12 and guesserWins == False:
            Master.CreateSecretLine(grid)
            Guesser.GuessSecretLine(grid,1)
            guesserWins = grid.CorrectLine(1)
            turn += 1
        
        print("game finish")
        if guesserWins == True :
            print("guesser wins")
        else :
            print("master winner")