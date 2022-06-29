import sys
from time import sleep
#do this first-->py -m pip install --user pygame
#from python crash course by eric matthes
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """class to run the program"""

#constructor
    def __init__(self) :
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        #start main loop for game
        while True:
            #check if keyboard or mouse wants it to quit
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit();
            #redo the screen
            pygame.display.flip()

if __name__== '__main__':
    ai=AlienInvasion
    ai.run_game()