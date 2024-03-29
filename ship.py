import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #Load the ship image and get its rect.
        DEFAULT_IMAGE_SIZE = (64, 48)
        image = pygame.image.load("images/ship.png")
        self.image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of teh screen
        self.rect.midbottom = self.screen_rect.midbottom
        #store a decimal value for teh ship's horizontal position
        self.x = float(self.rect.x)
        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update moving the ships position based on the movement flag"""
        #updates the ships x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update the rect object from self.x
        self.rect.x = self.x
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)