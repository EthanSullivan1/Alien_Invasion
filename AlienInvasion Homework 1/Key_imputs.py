import pygame
from time import sleep
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.flip()
while True:
    new_event = pygame.event.get()
    print(new_event)
    sleep(1)