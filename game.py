from line import Line
from piece import Piece, ColorCombinaison
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
        colors = [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW]
        Master.CreateSecretLine(grid)
            
        while turn <= 12 and guesserWins == False:
            print("BEGIN Turn number  ", turn)
            #TODO supprimer print
            Guesser.GuessSecretLine(grid,turn, colors)
            #TODO pass by player like createsecretline and guesssecretline or delete player.py
            guesserWins = grid.CorrectLine(turn, colors)
            turn += 1
            
        print("game finish")
        if guesserWins == True :
            print("guesser wins")
        else :
            print("master winner")