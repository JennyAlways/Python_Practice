import pygame
import random

SCREENWIDTH = 800
SCREENHEIGHT = 600

pygame.init()

screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])

RED = (255, 0, 0)

keepGoing = True
number = 0

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    if number < 10:
        keepGoing = True
        x = random.randint(0, SCREENWIDTH)
        y = random.randint(0, SCREENHEIGHT)
        spot = (x, y)
        pygame.draw.circle(screen, RED, spot, 30)
        number += 1

    print number

    pygame.display.update()

pygame.quit()
