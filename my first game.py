import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
running=True
while running :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill((255,240,230))
    pygame.draw.circle(screen,(0,0,255),(200,200),60)
    pygame.display.flip()
pygame.quit()
