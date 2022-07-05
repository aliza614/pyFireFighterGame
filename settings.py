class Settings:
    def __init__(self):
    #initializes the game's attributes controlling the game appearance and the ship's speed
        # screen settings
        self.screen_width=1000
        self.screen_height=400
        self.bg_color=(255,192,203)
        #ffc0cb is the hexadecimal for this color above
        
        #ship settings
        self.ship_speed=1.5
        self.ship_limit=3

        #water settings
        self.water_speed=1.5
        self.water_width=3
        self.water_height=15
        self.water_color=(9, 195, 219)
        self.waters_allowed=3

        #fire speed
        self.fire_speed=1.0
        self.fires_direction=1
        #1 is right -1 is left
        self.fire_drop_speed=10

        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed=1.5
        self.water_speed=3.0
        self.fire_speed=1.0
        self.fires_direction=1
        self.fire_points=50

    def increase_speed(self):
        self.ship_speed*=self.speedup_scale
        self.water_speed*=self.speedup_scale
        self.fire_speed*=self.speedup_scale
        self.fire_points=int(self.fire_points*self.score_scale)
        print(self.fire_points)