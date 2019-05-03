import pygame
import sys
from box import Box
from road import Road
from road_2 import Road_2
from pond import Pond
from arrow import Arrow
from tower import Tower
from fan import Fan
from tree import Tree
from flower import Flower
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Avengers Tower Defense")

def images():

	global cone
	global flower
	global tree
	global grass
	global tile
	global tile_2
	global tile_3
	global tile_4
	global background
	global steel
	global logo
	box = pygame.image.load('resources/box.png')
	cone = pygame.image.load('resources/cone.png')
	flower = pygame.image.load('resources/flower.png')
	tree = pygame.image.load('resources/tree.png')
	grass = pygame.image.load('resources/grass.jpg')
	tile = pygame.image.load('resources/tile.jpg')
	tile_2 = pygame.image.load('resources/tile(2).jpg')
	tile_3 = pygame.image.load('resources/tile(3).jpg')
	tile_4 = pygame.image.load('resources/tile(4).jpg')
	background = pygame.image.load('resources/background.jpg')
	logo = pygame.image.load('resources/logo.png')
	steel = pygame.image.load('resources/steel.jpg')

def map_sprites():

	global h_roads
	global v_roads
	global boxes
	global towers
	global fans
	global trees
	global flowers
	global pond
	global arrow
	h_roads = pygame.sprite.Group()
	v_roads = pygame.sprite.Group()
	boxes = pygame.sprite.Group()
	towers = pygame.sprite.Group()
	fans = pygame.sprite.Group()
	trees = pygame.sprite.Group()
	flowers = pygame.sprite.Group()
	h_roads.add(Road(0, 75))
	h_roads.add(Road(0, 375))
	h_roads.add(Road(0, 675))
	v_roads.add(Road_2(150, 0))
	v_roads.add(Road_2(350, 0))
	v_roads.add(Road_2(550, 0))
	v_roads.add(Road_2(750, 0))
	boxes.add(Box(5, 5))
	boxes.add(Box(495, 20))
	boxes.add(Box(295, 320))
	boxes.add(Box(95, 130))
	boxes.add(Box(605, 320))
	boxes.add(Box(205, 620))
	boxes.add(Box(695, 430))
	boxes.add(Box(945, 620))
	boxes.add(Box(405, 730))
	boxes.add(Box(805, 745))
	towers.add(Tower(0, 275))
	towers.add(Tower(200, 125))
	towers.add(Tower(950, 275))
	towers.add(Tower(300, 575))
	fans.add(Fan(700, 125))
	fans.add(Fan(950, 125))
	fans.add(Fan(0, 625))
	fans.add(Fan(600, 625))
	fans.add(Fan(300, 0))
	fans.add(Fan(200, 750))
	trees.add(Tree(400, 125))
	trees.add(Tree(500, 625))
	flowers.add(Flower(405, 325))
	flowers.add(Flower(530, 325))
	flowers.add(Flower(465, 300))
	flowers.add(Flower(405, 460))
	flowers.add(Flower(530, 460))
	flowers.add(Flower(465, 480))
	pond = Pond(400, 325)
	arrow = Arrow(875, 25)

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
	DISPLAYSURF.blit(logo, (5, 730))
	DISPLAYSURF.blit(background, (1000, 0))
	DISPLAYSURF.blit(pond.image, pond.rect)
	DISPLAYSURF.blit(arrow.image, arrow.rect)
	for v in v_roads:
		DISPLAYSURF.blit(v.image, v.rect)
	for h in h_roads:
		DISPLAYSURF.blit(h.image, h.rect)
	for b in boxes:
		DISPLAYSURF.blit(b.image, b.rect)
	for t in towers:
		DISPLAYSURF.blit(t.image, t.rect)
	for f in fans:
		DISPLAYSURF.blit(f.image, f.rect)
	for tr in trees:
		DISPLAYSURF.blit(tr.image, tr.rect)
	for fl in flowers:
		DISPLAYSURF.blit(fl.image, fl.rect)
	DISPLAYSURF.blit(cone, (150, 25))
	DISPLAYSURF.blit(cone, (100, 75))
	DISPLAYSURF.blit(cone, (100, 375))
	DISPLAYSURF.blit(cone, (150, 425))
	DISPLAYSURF.blit(cone, (750, 325))
	DISPLAYSURF.blit(cone, (800, 375))
	DISPLAYSURF.blit(cone, (750, 725))
	DISPLAYSURF.blit(cone, (800, 675))
	pygame.draw.line(DISPLAYSURF, (255, 255, 255), (1000, 0), (1000, 800), 10)

images()
map_sprites()

while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	draw_map()
	pygame.display.update()
