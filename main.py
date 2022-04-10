import logging
from game import Game
from logger import Logger

numberGame = 1 

log = Logger(logging.INFO, '%(levelname)s: %(asctime)s | %(message)s ', 'utf-8', 'mastermind.log')
log.LogInInfoLevel("Start games!!!")
while numberGame <= 20 :
    log.LogInInfoLevel("Partie %s" % numberGame)
    game = Game(log)
    game.Play()
    numberGame += 1
log.LogInInfoLevel("Game is finish!!!")