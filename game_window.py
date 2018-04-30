import pygame

x = int(input("How many pixels wide do you want the window resolution to be?"))
y = int(input("How many pixels tall do you want the window resolution to be?"))
screen = pygame.display.set_mode((x, y))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	screen.fill((0,0,0))
	pygame.display.flip()