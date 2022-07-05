import sys
sys.executable
from time import sleep
#do this first-->
# python --version
# pip --version
# pip install --user pygame
#from python crash course by eric matthes
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from water import Water
from fire import Fire

class FireFighter:
    """class to run the program"""

#constructor
    def __init__(self) :
        pygame.init()
        self.settings=Settings()

        self.screen=pygame.display.set_mode(
            (0,0), pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Fire Fighter")
        
        self.stats=GameStats(self)
        self.sb=ScoreBoard(self)

        self.ship=Ship(self)
        self.waters=pygame.sprite.Group()
        self.fires=pygame.sprite.Group()
        self._create_fires()
        #set background color
        #now defined in settings
        #self.bg_color=(230,230,230)
        self.play_button=Button(self,"Play")

    def run_game(self):
        #start main loop for game
        while True:
            #check if keyboard or mouse wants it to quit
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_waters()
                self._update_fires()
            self._update_screen()
            
    def _check_events(self):
    #handle key and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            self._check_keydown_events(event)
            self._check_keyup_events(event)
                
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.sb.check_high_score()
            self.stats.reset_stats()
            self.stats.game_active=True
            self.sb.prep_score()
            self.waters.empty()
            self.fires.empty()
            self._create_fires()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.settings.initialize_dynamic_settings()

    def _check_keydown_events(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                self.ship.moving_left=True
            elif event.key==pygame.K_q or event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_SPACE:
                self._shoot_water()

    def _check_keyup_events(self, event):
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                self.ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                self.ship.moving_left=False

    def _shoot_water(self):
        if len(self.waters)<self.settings.waters_allowed:
            new_water=Water(self)
            self.waters.add(new_water)
        

    def _update_screen(self):
        #redraw screen for each pass through loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #redo the screen
        for water in self.waters.sprites():
            water.draw_water()
        self.fires.draw(self.screen)
        self.sb.show_score()
        
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _update_waters(self):
        #update position of waters and get rid of old waters
        self.waters.update()

            #get rid of water that has disappeared
        for water in self.waters.copy():
            if water.rect.bottom<=0:
                self.waters.remove(water)
        #to test length of waters array -->print(len(self.waters))    
        self._check_water_fire_collisions()

    def _check_water_fire_collisions(self):
        collisions=pygame.sprite.groupcollide(self.waters, self.fires, True,True)
        if collisions:
            for fires in collisions.values():
                self.stats.score+=self.settings.fire_points*len(fires)
            self.sb.prep_score()
        if not self.fires:
            self.waters.empty()
            self._create_fires()
            self.settings.increase_speed()

    def _update_fires(self):

        self._check_fires_edges()
        collisions=pygame.sprite.groupcollide(self.waters, self.fires, True, True)
        if not self.fires:
            self.waters.empty()
            self._create_fires()
        self.fires.update()
        if pygame.sprite.spritecollideany(self.ship, self.fires):
            self._ship_hit()
        self._check_fires_bottom()

    def _create_fires(self):
        fire=Fire(self)
        fire_width=fire.rect.width
        fire_height=fire.rect.height
        available_space_x=self.settings.screen_width-(2*fire_width)
        available_space_y=self.settings.screen_height-(3*fire_height)-self.ship.rect.height
        number_fires_x=available_space_x//(fire_width*2)
        number_rows=available_space_y//(fire_height*2)
        #create first row of fires
        for row_number in range(3):
            for fire_number in range(number_fires_x):
                self._create_fire(fire_number, row_number)
                
    def _create_fire(self,fire_number, row_number):
        fire=Fire(self)
        fire_width=fire.rect.width
        fire_height=fire.rect.height
        fire.x=fire_width+2*fire_width*fire_number
        fire.rect.x=fire.x
        fire.y=fire_height+2*fire_height*row_number
        fire.rect.y=fire.y
        self.fires.add(fire)
    def _check_fires_edges(self):
        for fire in self.fires.sprites():
            if fire.check_edges():
                self._change_fires_direction()
                break
    def _change_fires_direction(self):
        for fire in self.fires.sprites():
            fire.rect.y+=self.settings.fire_drop_speed
        self.settings.fires_direction*=-1

    def _ship_hit(self):
        if self.stats.ships_left>0:
            self.stats.ships_left-=1
            self.fires.empty()
            self.waters.empty()

            self._create_fires()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)
            
    def _check_fires_bottom(self):
        screen_rect=self.screen.get_rect()
        for fire in self.fires.sprites():
            if fire.rect.bottom>=screen_rect.bottom:
                self._ship_hit()
                break
            
if __name__== '__main__':
    ff=FireFighter()
    ff.run_game()
