import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("Sphinx")

sphinx_pic = pygame.image.load("images/sphinx.png")
odeipus_pic = pygame.image.load("images/oedipus.png")

keep_going = True

while keep_going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False

	screen.blit(sphinx_pic,(40,50))
	screen.blit(odeipus_pic, (150,350))

	pygame.display.update()

pygame.quit()
