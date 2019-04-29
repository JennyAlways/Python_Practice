import pygame
import time
import random

SCREENWIDTH = 756
SCREENHEIGHT = 650

pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
pygame.display.set_caption("Create chick")

keepGoing = True

interval = 25
cool_down = interval

chick_img = pygame.image.load("images/chick.png")
BG = pygame.image.load("images/background.png")
chick_lose = pygame.image.load("images/chicklose.png")
egg_shell = pygame.image.load("images/eggshell.png")
chick_win = pygame.image.load("images/chickwin.png")

chick_height = 51
chick_width = 50
shell_height = 46
shell_width = 65

chick_x = []
chick_y = []
shell_x = 100
shell_y = SCREENHEIGHT - shell_height


def chick_catch(x, y):
    if y + chick_height >= shell_y and x >= shell_x \
            and x + chick_width < shell_x + shell_width:
        return True
    else:
        return False


while keepGoing:

    screen.blit(BG, (0, 0))

    temp_chick_x = []
    temp_chick_y = []

    for i in range(len(chick_y)):
        if chick_y[i] <= SCREENHEIGHT - chick_height:
            temp_chick_x.append(chick_x[i])
            temp_chick_y.append(chick_y[i] + 10)

    chick_x = temp_chick_x
    chick_y = temp_chick_y

    cool_down -= 1

    if cool_down == 0:
        x = random.randint(0, SCREENWIDTH)
        chick_x.append(x)
        chick_y.append(0)
        cool_down = interval

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_RIGHT:
                shell_x += 10
            elif key == pygame.K_LEFT:
                shell_x -= 10

    for i in range(len(chick_x)):
        if chick_catch(chick_x[i], chick_y[i]):
            screen.blit(chick_win, (chick_x[i], chick_y[i]))
        elif chick_y[i] > SCREENHEIGHT - chick_height:
            screen.blit(chick_lose, (chick_x[i], chick_y[i]))
        else:
            screen.blit(chick_img, (chick_x[i], chick_y[i]))

    screen.blit(egg_shell, (shell_x, shell_y))

    pygame.display.update()

pygame.quit()
