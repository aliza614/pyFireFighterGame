import pygame

class Ship:
# this class controls the spaceship
    def __init__(self,ai_game) :
        #initialize the ship with starting postion
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings

        #load ship image and get it's rect
        self.image=pygame.image.load('img\ship-pink.bmp')
        self.rect=self.image.get_rect()
        
        #make ship start at the bottom center of the screen
        self.rect.midbottom=self.screen_rect.midbottom
    
        #store a decimal value for ship's horizontal position
        self.x=float(self.rect.x)
        #Movement flag
        self.moving_right=False
        self.moving_left=False
    
    def update(self):
    #manages the ship's postition
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        elif self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        self.rect.x=self.x
        
    #draw ship at current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
    