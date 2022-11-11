import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represents a single alien in the fleet"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and sets its rect
        DEFAULT_IMAGE_SIZE = (30, 30)
        image = pygame.image.load("../images/raindrop.png")
        self.image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screeb
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store each alien horizontal pos
        self.y = float(self.rect.y)

    def check_disappeared(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """moves the alien"""
        self.y += (self.settings.alien_speed)
        self.rect.y = self.y
    # def check_edges(self):
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.right >= screen_rect.right or self.rect.left <= 0:
    #         return True

