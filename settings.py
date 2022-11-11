class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (0,0,0)

        #ship speed
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.5
        self.ship_limit = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (57, 255, 20)
        self.bullets_allowed = 55

        #alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 = right and -1 = left
        self.fleet_direction = 1
