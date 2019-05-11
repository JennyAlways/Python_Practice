import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("pong!")

def main():
    ball = pygame.image.load("images/ball.png")

    ball_x = 400
    ball_y = 300

    ball_d =20

    ball_x_speed = 5
    ball_y_speed =10

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ball_x += ball_x_speed
        ball_y += ball_y_speed

        screen.fill((0,0,0))
        screen.blit(ball, (ball_x, ball_y))
        pygame.display.update()


main()
pygame.quit()