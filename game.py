from line import Line
from player import PlayerType, Player

#TODO : change class name to board
class Game: 
    def __init__(self) :
        self.players = ["player1" , "player2"]
    
    #TODO : manage all game
    def Play(self):
       Master = Player(PlayerType.MASTER)
       Master.CreateSecretLine()
       Guesser = Player(PlayerType.GUESSER)
       Guesser.GuessSecretLine(1)