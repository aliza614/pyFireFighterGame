import pygame
from pygame.sprite import Sprite

class Fire(Sprite):
    #class to represent single fire in fires

    def __init__(self, ff_game):
        super().__init__()
        self.screen=ff_game.screen
        self.settings=ff_game.settings

        #load fire images
        self.image=pygame.image.load('img/fire-pink-cropped.bmp')
        self.rect=self.image.get_rect()

        #start with each new fire at top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #store fire's exact horizonal position
        self.x=float(self.rect.x)

    def update(self):
        self.x+=(self.settings.fires_direction*self.settings.fire_speed)
        self.rect.x=self.x

    
    def check_edges(self):
        #return true if alien is at edge of screen
        screen_rect=self.screen.get_rect()
        if self.rect.right>screen_rect.right or self.rect.left<screen_rect.left:
            return True