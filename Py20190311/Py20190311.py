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

Color = [RED,GREEN,BLUE]

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    if not haddrawn:
        for a in range(100):
            pencolor = Color [a%3]
            x = random.randint(0,SCREENWIDTH)
            y = random.randint(0,SCREENHEIGHT)
            pygame.draw.circle(screen, pencolor, (x, y), 50)

        haddrawn = True

    pygame.display.update()

pygame.quit()






