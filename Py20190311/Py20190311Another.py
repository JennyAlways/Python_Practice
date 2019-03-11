import pygame
import random

SCREENWIDTH = 800
SCREENHEIGHT = 600

pygame.init()

screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
pygame.display.set_caption("Draw a Circle")

keepGoing = True
haddrawn = False

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

Color = RED

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            spot = event.pos
            pygame.draw.circle(screen,Color,spot,50)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Color = RED
            elif event.key == pygame.K_g:
                Color = GREEN
            elif  event.key == pygame.K_b:
                Color = BLUE

    pygame.display.update()

pygame.quit()






