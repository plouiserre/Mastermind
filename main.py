import logging
from game import Game
from logger import Logger

numberGame = 1 

log = Logger(logging.DEBUG, '%(levelname)s: %(asctime)s | %(message)s ', 'utf-8', 'mastermind.log')
log.LogInDebugLevel("Start games!!!")
while numberGame <= 20 :
    log.LogInDebugLevel("Partie %s" % numberGame)
    game = Game()
    game.Play()
    numberGame += 1
log.LogInDebugLevel("Game is finish!!!")