import pygame
import sys
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1300, 900))
pygame.display.set_caption("Avengers Tower Defense")
DISPLAYSURF.fill((200, 200, 200))

def variables():

	global box
	global cone
	global fan
	global flower
	global tree
	global water
	box = pygame.image.load('resources/box.png')
	cone = pygame.image.load('resources/cone.jpg')
	fan = pygame.image.load('resources/fan.png')
	flower = pygame.image.load('resources/flower.jpg')
	tree = pygame.image.load('resources/tree.png')
	water = pygame.image.load('resources/water.png')

def draw_map():

	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (0, 0, 150, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (200, 0, 150, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (400, 0, 150, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (600, 0, 150, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (800, 0, 200, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (0, 175, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (200, 175, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (0, 200, 0), (400, 175, 150, 550))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (600, 175, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (800, 175, 200, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (0, 475, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (200, 475, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (600, 475, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (800, 475, 200, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (0, 775, 150, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (200, 775, 150, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (400, 775, 150, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (600, 775, 150, 125))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (800, 775, 200, 125))
	pygame.draw.circle(DISPLAYSURF, (0, 0, 200), (475, 450), 75, 75)
	pygame.draw.line(DISPLAYSURF, (200, 200, 200), (400, 450), (550, 450), 50)
	DISPLAYSURF.blit(box, (5, 5))
	DISPLAYSURF.blit(box, (495, 70))
	DISPLAYSURF.blit(box, (805, 70))
	DISPLAYSURF.blit(box, (95, 180))
	DISPLAYSURF.blit(box, (295, 370))
	DISPLAYSURF.blit(box, (605, 370))
	DISPLAYSURF.blit(box, (205, 670))
	DISPLAYSURF.blit(box, (695, 480))
	DISPLAYSURF.blit(box, (945, 670))
	DISPLAYSURF.blit(box, (5, 780))
	DISPLAYSURF.blit(box, (405, 780))
	DISPLAYSURF.blit(box, (805, 845))

variables()

while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	draw_map()
	pygame.display.update()
