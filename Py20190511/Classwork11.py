import pygame
from color_ball import *

# initialize the game
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Colorful Balls")

# colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    # TODO: instantiate balls
    ball1 = Color_Ball(WHITE, 5, 100, 100, 5, 6)
    ball2 = Color_Ball(RED, 3, 230, 132, 7, 9)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # TODO: move balls
        ball1.move()
        ball2.move()

        screen.fill(BLACK)
        # TODO: draw balls
        ball1.draw(screen)
        ball2.draw(screen)

        pygame.display.update()


main()
pygame.quit()
