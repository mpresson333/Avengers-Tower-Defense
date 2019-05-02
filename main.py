import pygame
import sys
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Avengers Tower Defense")
DISPLAYSURF.fill((200, 200, 200))

def variables():

	global box
	global cone
	global fan
	global flower
	global tree
	global water
	global road
	global road_2
	global grass
	global water_2
	global tile
	global tile_2
	global tile_3
	global tile_4
	global background
	global steel
	global logo
	global arrow
	box = pygame.image.load('resources/box.png')
	cone = pygame.image.load('resources/cone.png')
	fan = pygame.image.load('resources/fan.png')
	flower = pygame.image.load('resources/flower.png')
	tree = pygame.image.load('resources/tree.png')
	water = pygame.image.load('resources/water.png')
	road = pygame.image.load('resources/road.jpg')
	road_2 = pygame.image.load('resources/road(2).jpg')
	grass = pygame.image.load('resources/grass.jpg')
	water_2 = pygame.image.load('resources/water(2).png')
	tile = pygame.image.load('resources/tile.jpg')
	tile_2 = pygame.image.load('resources/tile(2).jpg')
	tile_3 = pygame.image.load('resources/tile(3).jpg')
	tile_4 = pygame.image.load('resources/tile(4).jpg')
	background = pygame.image.load('resources/background.jpg')
	logo = pygame.image.load('resources/logo.png')
	steel = pygame.image.load('resources/steel.jpg')
	arrow = pygame.image.load('resources/arrow.png')

def draw_map():

	DISPLAYSURF.blit(tile, (0, 0))
	DISPLAYSURF.blit(tile, (200, 0))
	DISPLAYSURF.blit(tile, (400, 0))
	DISPLAYSURF.blit(tile, (600, 0))
	DISPLAYSURF.blit(steel, (0, 725))
	DISPLAYSURF.blit(tile, (200, 725))
	DISPLAYSURF.blit(tile, (400, 725))
	DISPLAYSURF.blit(tile, (600, 725))
	DISPLAYSURF.blit(tile_4, (800, 0))
	DISPLAYSURF.blit(tile_4, (800, 725))
	DISPLAYSURF.blit(tile_3, (0, 125))
	DISPLAYSURF.blit(tile_3, (200, 125))
	DISPLAYSURF.blit(tile_3, (600, 125))
	DISPLAYSURF.blit(tile_2, (800, 125))
	DISPLAYSURF.blit(tile_3, (0, 425))
	DISPLAYSURF.blit(tile_3, (200, 425))
	DISPLAYSURF.blit(tile_3, (600, 425))
	DISPLAYSURF.blit(tile_2, (800, 425))
	DISPLAYSURF.blit(grass, (400, 125))
	DISPLAYSURF.blit(grass, (400, 425))
	DISPLAYSURF.blit(water_2, (400, 325))
	DISPLAYSURF.blit(road_2, (150, 0))
	DISPLAYSURF.blit(road_2, (350, 0))
	DISPLAYSURF.blit(road_2, (550, 0))
	DISPLAYSURF.blit(road_2, (750, 0))
	DISPLAYSURF.blit(road, (0, 75))
	DISPLAYSURF.blit(road, (0, 375))
	DISPLAYSURF.blit(road, (0, 675))
	DISPLAYSURF.blit(box, (5, 5))
	DISPLAYSURF.blit(box, (495, 20))
	DISPLAYSURF.blit(arrow, (875, 25))
	DISPLAYSURF.blit(box, (95, 130))
	DISPLAYSURF.blit(box, (295, 320))
	DISPLAYSURF.blit(box, (605, 320))
	DISPLAYSURF.blit(box, (205, 620))
	DISPLAYSURF.blit(box, (695, 430))
	DISPLAYSURF.blit(box, (945, 620))
	DISPLAYSURF.blit(logo, (5, 730))
	DISPLAYSURF.blit(box, (405, 730))
	DISPLAYSURF.blit(box, (805, 745))
	DISPLAYSURF.blit(cone, (150, 25))
	DISPLAYSURF.blit(cone, (100, 75))
	DISPLAYSURF.blit(cone, (100, 375))
	DISPLAYSURF.blit(cone, (150, 425))
	DISPLAYSURF.blit(cone, (750, 325))
	DISPLAYSURF.blit(cone, (800, 375))
	DISPLAYSURF.blit(cone, (750, 725))
	DISPLAYSURF.blit(cone, (800, 675))
	DISPLAYSURF.blit(background, (1000, 0))
	DISPLAYSURF.blit(water, (0, 275))
	DISPLAYSURF.blit(water, (200, 125))
	DISPLAYSURF.blit(water, (950, 275))
	DISPLAYSURF.blit(water, (300, 575))
	DISPLAYSURF.blit(fan, (700, 125))
	DISPLAYSURF.blit(fan, (950, 125))
	DISPLAYSURF.blit(fan, (0, 625))
	DISPLAYSURF.blit(fan, (600, 625))
	DISPLAYSURF.blit(fan, (300, 0))
	DISPLAYSURF.blit(fan, (200, 750))

variables()

while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	draw_map()
	pygame.display.update()
