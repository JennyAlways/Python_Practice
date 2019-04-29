import pygame

SCREENWIDTH = 756
SCREENHEIGHT = 650

pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
pygame.display.set_caption("Create chick")

keepGoing = True


chick_img = pygame.image.load("images/chick.png")
BG = pygame.image.load("images/background.png")
chick_lose = pygame.image.load("images/chicklose.png")

chick_height = 51
chick_width = 50

chick_x = []
chick_y = []

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
        if chick_y[i] > SCREENHEIGHT - chick_height:
            screen.blit(chick_lose, (chick_x[i], chick_y[i]))
        else:
            screen.blit(chick_img, (chick_x[i], chick_y[i]))


    pygame.display.update()

pygame.quit()