import pygame
import sys
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1300, 800))
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
	cone = pygame.image.load('resources/cone.png')
	fan = pygame.image.load('resources/fan.png')
	flower = pygame.image.load('resources/flower.jpg')
	tree = pygame.image.load('resources/tree.png')
	water = pygame.image.load('resources/water.png')

def draw_map():

	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (0, 0, 150, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (200, 0, 150, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (400, 0, 150, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (600, 0, 150, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (800, 0, 200, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (0, 125, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (200, 125, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (0, 200, 0), (400, 125, 150, 550))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (600, 125, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (800, 125, 200, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (0, 425, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (200, 425, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (600, 425, 150, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (800, 425, 200, 250))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (0, 725, 150, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (200, 725, 150, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (400, 725, 150, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (600, 725, 150, 75))
	pygame.draw.rect(DISPLAYSURF, (128, 128, 128), (800, 725, 200, 75))
	pygame.draw.circle(DISPLAYSURF, (0, 0, 200), (475, 400), 75, 75)
	pygame.draw.line(DISPLAYSURF, (200, 200, 200), (400, 400), (550, 400), 50)
	DISPLAYSURF.blit(box, (5, 5))
	DISPLAYSURF.blit(box, (495, 20))
	DISPLAYSURF.blit(box, (805, 20))
	DISPLAYSURF.blit(box, (95, 130))
	DISPLAYSURF.blit(box, (295, 320))
	DISPLAYSURF.blit(box, (605, 320))
	DISPLAYSURF.blit(box, (205, 620))
	DISPLAYSURF.blit(box, (695, 430))
	DISPLAYSURF.blit(box, (945, 620))
	DISPLAYSURF.blit(box, (5, 730))
	DISPLAYSURF.blit(box, (405, 730))
	DISPLAYSURF.blit(box, (805, 745))
	DISPLAYSURF.blit(cone, (150, 25))
	DISPLAYSURF.blit(cone, (100, 75))
	DISPLAYSURF.blit(cone, (100, 375))
	DISPLAYSURF.blit(cone, (150, 425))
	DISPLAYSURF.blit(cone, (150, 25))
	DISPLAYSURF.blit(cone, (150, 25))
	DISPLAYSURF.blit(cone, (150, 25))
	DISPLAYSURF.blit(cone, (150, 25))

variables()

while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	draw_map()
	pygame.display.update()
