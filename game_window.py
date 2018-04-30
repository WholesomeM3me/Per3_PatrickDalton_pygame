import pygame

x = int(input("How wide do you want the window resolution to be in pixels?"))
y = int(input("How tall do you want the window resolution to be?"))
screen = pygame.display.set_mode((x, y))
running = True

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False