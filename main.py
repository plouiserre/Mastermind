import logging
from game import Game
from logger import Logger


log = Logger(logging.INFO, '%(levelname)s: %(asctime)s | %(message)s ', 'utf-8', 'mastermind.log')

log.LogInInfoLevel("Start games!!!")
game = Game(log)
game.Play()
log.LogInInfoLevel("Game is finish!!!")