class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (255,255,255)

        #alien Settings
        self.alien_speed =3
        self.fleet_drop_speed = 2
        #fleet direction of 1 = right and -1 = left
        self.fleet_direction = 1
