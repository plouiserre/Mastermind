from line import Line
from piece import Piece, ColorCombinaison
#TODO : à supprimer
from grid import Grid

#TODO : change class name to board
class Game: 
    def __init__(self) :
        self.players = ["player1" , "player2"]
    
    #TODO : manage all game
    def Play(self):
        grid = Grid()
        turn = 1 
        guesserWins = False
        grid.CreateSecretLine()
            
        while turn <= 12 and guesserWins == False:
            #TODO supprimer print
            print("\n\nBEGIN Turn number  ", turn)
            grid.GuessLine(turn)
            #TODO pass by player like createsecretline and guesssecretline or delete player.py
            guesserWins = grid.CorrectLine(turn)
            turn += 1
            
        print("game finish")
        if guesserWins == True :
            print("guesser wins")
        else :
            print("master winner")