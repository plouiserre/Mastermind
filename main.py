from game import Game

numberGame = 0 
while numberGame < 20 : 
    print("-------------------------------")
    print("Partie ", numberGame)
    game = Game()
    game.Play()
    numberGame += 1
    print("-------------------------------")
