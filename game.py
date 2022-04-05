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
        colors = { 0 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                1 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                2 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW], 
                3 : [ColorCombinaison.BLUE, ColorCombinaison.GREEN, ColorCombinaison.ORANGE, ColorCombinaison.PURPLE, 
                    ColorCombinaison.RED, ColorCombinaison.PINK, ColorCombinaison.YELLOW]}
        grid.CreateSecretLine()
            
        while turn <= 12 and guesserWins == False:
            #TODO supprimer print
            print("\n\nBEGIN Turn number  ", turn)
            grid.GuessLine(turn, colors)
            #TODO pass by player like createsecretline and guesssecretline or delete player.py
            guesserWins = grid.CorrectLine(turn, colors)
            turn += 1
            
        print("game finish")
        if guesserWins == True :
            print("guesser wins")
        else :
            print("master winner")