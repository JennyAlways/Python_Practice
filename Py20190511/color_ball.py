import pygame


class Color_Ball:
    def __init__(self, color, radius, x, y, x_speed, y_speed):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
