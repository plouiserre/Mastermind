import logging
from game import Game
from logger import Logger


log = Logger(logging.INFO, '%(levelname)s: %(asctime)s | %(message)s ', 'utf-8', 'mastermind.log')

log.Log_Info_Level("Start games!!!")
game = Game(log)
game.play()
log.Log_Info_Level("Game is finish!!!")