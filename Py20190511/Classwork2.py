import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("pong!")


def main():
    paddle = pygame.image.load("images/paddle.png")
    paddle_width = 100
    paddle_height =25
    paddle_x =400
    paddle_y =SCREEN_HEIGHT - paddle_height -5

    ball = pygame.image.load("images/ball.png")
    BG = pygame.image.load("images/bg.jpg")

    ball_x = 400
    ball_y = 300

    ball_d = 20

    ball_x_speed = 5
    ball_y_speed = 10

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                key =event.key
                if key == pygame.K_RIGHT:
                    paddle_x += 10
                elif key == pygame.K_LEFT:
                    paddle_x -= 10

        if ball_x <= 0 or ball_x + ball_d >= SCREEN_WIDTH:
            ball_x_speed *= -1

        if ball_y <= 0 or ball_y + ball_d >= SCREEN_HEIGHT:
            ball_y_speed *= -1


        ball_x += ball_x_speed
        ball_y += ball_y_speed

        screen.blit(BG, (0,0))
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(paddle, (paddle_x, paddle_y))
        pygame.display.update()


main()
pygame.quit()
