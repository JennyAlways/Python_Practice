import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("Arial", 20)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Sphinx")

sphinx_pic = pygame.image.load("images/sphinx.png")
odeipus_pic = pygame.image.load("images/oedipus.png")
win_pic = pygame.image.load("images/win.png")
eat_pic = pygame.image.load("images/eat.png")

keep_going = True

answer_x = 350
answer_y = 360
answer = ""
result = win_pic
GAME = 1
END = 2
game_state = GAME


while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_state = END
            elif event.key >=97 and event.key<=122:
                answer += chr(event.key)
            elif event.key == pygame.K_BACKSPACE:
                answer =answer[:len(answer)-1]
                pygame.display.update()


    if game_state == GAME:
        screen.fill((0, 0, 0))
        key = myfont.render(answer, False, (255, 255, 255))
        screen.blit(key, (answer_x, answer_y))

        riddle1 = myfont.render("Who are you", False, (255, 255, 255))
        riddle2 = myfont.render("Who are you", False, (255, 255, 255))
        riddle3 = myfont.render("Who are you", False, (255, 255, 255))

        screen.blit(riddle1, (320, 200))
        screen.blit(riddle2, (320, 230))
        screen.blit(riddle3, (320, 260))

        screen.blit(sphinx_pic, (40, 50))
        screen.blit(odeipus_pic, (150, 350))


    if game_state == END:
        screen.fill((0, 0, 0))
        if answer == "man":
            screen.blit(win_pic, (250, 150))
            result = myfont.render("You've won the game!",False,(255,255,255))

        else:
            screen.blit(eat_pic, (250, 150))
            result = myfont.render("You lost!", False, (255, 255, 255))

        screen.blit(result,(160,170))


    pygame.display.update()


pygame.quit()
