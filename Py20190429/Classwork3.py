import pygame

SCREENWIDTH = 756
SCREENHEIGHT = 650

pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
pygame.display.set_caption("Create chick")

keepGoing = True


chick_img = pygame.image.load("images/chick.png")
BG = pygame.image.load("images/background.png")

chick_x = []
chick_y = []

while keepGoing:

    screen.blit(BG, (0,0))

    for i in range(len(chick_y)):
        chick_y[i] +=10

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           keepGoing = False
       elif event.type == pygame.MOUSEBUTTONDOWN:
           spot = event.pos
           chick_x.append(spot[0])
           chick_y.append(spot[1])
           print(chick_x)
           print(chick_y)

    for i in range(len(chick_x)):
        screen.blit(chick_img, (chick_x[i], chick_y[i]))

    pygame.display.update()

pygame.quit()