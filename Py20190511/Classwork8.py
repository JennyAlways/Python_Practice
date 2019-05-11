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

PLAYING = 1
END = 2

WHITE = (255, 255, 255)
font = pygame.font.SysFont("Stencil", 24)


def main():
    status = PLAYING
    score = 0
    lose1 = False
    lose2 = False

    # initialize paddle
    paddle = pygame.image.load("images/paddle.png")
    paddle_width = 100
    paddle_height = 25
    paddle_x = 400
    paddle_y = SCREEN_HEIGHT - paddle_height - 5
    paddle_speed = 0

    # initialize ball
    ball = pygame.image.load("images/ball.png")
    ball_x = 30
    ball_y = 50
    ball_d = 20
    ball_x_speed = 5
    ball_y_speed = 5

    ball2 = pygame.image.load("images/ball.png")
    ball2_x = 10
    ball2_y = 100
    ball2_d = 20
    ball2_x_speed = 5
    ball2_y_speed = 8

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

        if status == PLAYING:

            # ball position change
            if not lose1:
                if ball_y <= 0:
                    ball_y_speed *= -1
                if ball_x >= SCREEN_WIDTH - ball_d or ball_x <= 0:
                    ball_x_speed *= -1
                if ball_y + ball_d >= paddle_y:
                    if ball_x + (ball_d / 2) > paddle_x + paddle_width \
                            or ball_x + (ball_d / 2) < paddle_x:
                        lose1 = True
                    else:  # collide
                        ball_y_speed *= -1
                        score += 1

                ball_x += ball_x_speed
                ball_y += ball_y_speed

            # ball2 position change
            if not lose2:
                if ball2_y <= 0:
                    ball2_y_speed *= -1
                if ball2_x >= SCREEN_WIDTH - ball2_d or ball2_x <= 0:
                    ball2_x_speed *= -1
                if ball2_y + ball2_d >= paddle_y:
                    if ball2_x + (ball2_d / 2) > paddle_x + paddle_width \
                            or ball2_x + (ball2_d / 2) < paddle_x:
                        lose2 = True
                    else:  # collide
                        ball2_y_speed *= -1
                        score += 1

                ball2_x += ball2_x_speed
                ball2_y += ball2_y_speed

            if lose1 and lose2:
                status = END

            # paddle position change
            paddle_x += paddle_speed
            if paddle_x + paddle_width >= SCREEN_WIDTH:
                paddle_x = SCREEN_WIDTH - paddle_width
            if paddle_x <= 0:
                paddle_x = 0

            # draw
            screen.blit(bg, (0, 0))
            if not lose1:
                screen.blit(ball, (ball_x, ball_y))
            if not lose2:
                screen.blit(ball2, (ball2_x, ball2_y))
            screen.blit(paddle, (paddle_x, paddle_y))

            game_string = "Score: " + str(score)
            text = font.render(game_string, True, WHITE)
            screen.blit(text, (50, 50))

        pygame.display.update()


main()
pygame.quit()
