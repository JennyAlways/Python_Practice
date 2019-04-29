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

        if event.type == pygame.MOUSEBUTTONDOWN:
            spot = event.pos
            number += 1
            print number

            if number <= 10:
                keepGoing = True
                spot = event.pos
                pygame.draw.circle(screen, RED, spot, 30)

    pygame.display.update()

pygame.quit()
