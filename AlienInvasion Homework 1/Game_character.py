import pygame
from time import sleep

class Picture():
    def __init__(self,screen,image_address):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image_address)
        self.rect = self.image.get_rect()
    def draw(self):
        self.rect.center = self.screen_rect.center
        self.screen.blit(self.image, self.rect)



pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill((0, 0, 255))
ship =Picture(screen, "images/ship.bmp")
ship.draw()
pygame.display.flip()
sleep(10)