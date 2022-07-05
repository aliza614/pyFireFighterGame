import pygame 
from pygame.sprite import Sprite

class Water(Sprite):
    #a class to manage the water you shoot

    def __init__(self, ff_game):
        super().__init__()
        self.screen=ff_game.screen
        self.settings=ff_game.settings
        self.color=self.settings.water_color

        #create rect water at (0,0) then set to correct position
        self.rect=pygame.Rect(0,0,self.settings.water_width, self.settings.water_height)
        self.rect.midtop=ff_game.ship.rect.midtop

        #store water's position as a decimal value
        self.y=float(self.rect.y)
    
    def update(self):
        #make the water move up the screen
        self.y-=self.settings.water_speed
        #update rect position
        self.rect.y=self.y
    
    #draw water on screen
    def draw_water(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
