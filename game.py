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
       Master.CreateSecretLine(grid)
       Guesser = Player(PlayerType.GUESSER)
       Guesser.GuessSecretLine(grid,1)
       grid.CorrectLine(1)