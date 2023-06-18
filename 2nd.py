import pygame
from pygame.locals import (
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running=True

while running:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            running=False
    pygame.display.flip()

pygame.quit()
