import logging
from game import Game
from logger import Logger

numberGame = 0 

#logging.basicConfig(format ='%(levelname)s: %(asctime)s | %(message)s ' ,filename='mastermind.log', encoding='utf-8', level=logging.DEBUG)
#logging.warning("Hello world geeks!!!") 
log = Logger(logging.DEBUG, '%(levelname)s: %(asctime)s | %(message)s ', 'utf-8', 'mastermind.log')
log.LogInDebugLevel("Hello world geeks!!!")
while numberGame < 20 :
    print("-------------------------------")
    print("Partie ", numberGame)
    game = Game()
    game.Play()
    numberGame += 1
    print("-------------------------------")
