import pygame

# initialize the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Pong!")

# load images
# background
bg = pygame.image.load("images/bg.jpg")


def main():
    # initialize paddle
    paddle = pygame.image.load("images/paddle.png")
    paddle_width = 100
    paddle_height = 25
    paddle_x = 400
    paddle_y = SCREEN_HEIGHT - paddle_height - 5
    paddle_speed = 0

    # initialize ball
    ball = pygame.image.load("images/ball.png")
    ball_x = 400
    ball_y = 300
    ball_d = 20
    ball_x_speed = 5
    ball_y_speed = 10

    # main loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_RIGHT:
                    paddle_speed = 10
                elif key == pygame.K_LEFT:
                    paddle_speed = -10
            elif event.type == pygame.KEYUP:
                paddle_speed = 0

        # ball position change
        if ball_y <= 0:
            ball_y_speed *= -1
        if ball_y + ball_d >= paddle_y:
            if ball_x + (ball_d / 2) > paddle_x + paddle_width \
                    or ball_x + (ball_d / 2) < paddle_x:
                pass;
            else:
                ball_y_speed *= -1
        if ball_x >= SCREEN_WIDTH - ball_d or ball_x <= 0:
            ball_x_speed *= -1
        if ball_y + ball_d >= paddle_y:
            if ball_x + (ball_d / 2) > paddle_x + paddle_width \
                    or ball_x + (ball_d / 2) < paddle_x:
                lose = True
            else:  # collide
                ball_y_speed *= -1
        ball_x += ball_x_speed
        ball_y += ball_y_speed

        # paddle position change
        paddle_x += paddle_speed
        if paddle_x + paddle_width >= SCREEN_WIDTH:
            paddle_x = SCREEN_WIDTH - paddle_width
        if paddle_x <= 0:
            paddle_x = 0

        # draw
        screen.blit(bg, (0, 0))
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(paddle, (paddle_x, paddle_y))
        pygame.display.update()


main()
pygame.quit()
