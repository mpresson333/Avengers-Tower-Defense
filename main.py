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
from weak_bot import Weak_Bot
from blue_bot import Blue_Bot
from red_bot import Red_Bot
from ultron import Ultron
from widow import Widow
from cap import Cap
from thor import Thor
from tony import Tony
from hawkeye import Hawkeye
from hulk import Hulk
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Avengers Tower Defense")
FPS = 60
fpsClock = pygame.time.Clock()
bots = []

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
	global heart
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
	heart = pygame.image.load('resources/heart.png')

def map_sprites():

	global decorations
	decorations = pygame.sprite.Group()
	decorations.add(Pond(400, 325))
	decorations.add(Road_2(150, 0))
	decorations.add(Road_2(350, 0))
	decorations.add(Road_2(550, 0))
	decorations.add(Road_2(750, 0))
	decorations.add(Road(0, 75))
	decorations.add(Road(0, 375))
	decorations.add(Road(0, 675))
	decorations.add(Box(5, 5))
	decorations.add(Box(495, 20))
	decorations.add(Box(295, 320))
	decorations.add(Box(95, 130))
	decorations.add(Box(605, 320))
	decorations.add(Box(205, 620))
	decorations.add(Box(695, 430))
	decorations.add(Box(945, 620))
	decorations.add(Box(405, 730))
	decorations.add(Box(805, 745))
	decorations.add(Tower(0, 275))
	decorations.add(Tower(200, 125))
	decorations.add(Tower(950, 275))
	decorations.add(Tower(300, 575))
	decorations.add(Fan(700, 125))
	decorations.add(Fan(950, 125))
	decorations.add(Fan(0, 625))
	decorations.add(Fan(600, 625))
	decorations.add(Fan(300, 0))
	decorations.add(Fan(200, 750))
	decorations.add(Tree(400, 125))
	decorations.add(Tree(500, 625))
	decorations.add(Flower(405, 325))
	decorations.add(Flower(530, 325))
	decorations.add(Flower(465, 300))
	decorations.add(Flower(405, 460))
	decorations.add(Flower(530, 460))
	decorations.add(Flower(465, 480))
	decorations.add(Arrow(875, 25))

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
	DISPLAYSURF.blit(background, (1000, 100))
	for d in decorations:
		DISPLAYSURF.blit(d.image, d.rect)
	DISPLAYSURF.blit(cone, (150, 25))
	DISPLAYSURF.blit(cone, (100, 75))
	DISPLAYSURF.blit(cone, (100, 375))
	DISPLAYSURF.blit(cone, (150, 425))
	DISPLAYSURF.blit(cone, (750, 325))
	DISPLAYSURF.blit(cone, (800, 375))
	DISPLAYSURF.blit(cone, (750, 725))
	DISPLAYSURF.blit(cone, (800, 675))
	DISPLAYSURF.blit(heart, (1075, 20))

	pygame.draw.line(DISPLAYSURF, (255, 255, 255), (1000, 0), (1000, 800), 10)
	BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
	text = BASICFONT.render(str(lives), 1, (0,0,0))
	text_rect = text.get_rect()
	text_rect.topleft = (1100, 20)
	DISPLAYSURF.blit(text, text_rect)
	text = BASICFONT.render("$" + str(money), 1, (0,0,0))
	text_rect.topleft = (1085, 60)
	DISPLAYSURF.blit(text, text_rect)

def hero_sprites():

	global heroes
	widow = Widow()
	cap = Cap()
	tony = Tony()
	thor = Thor()
	hawkeye = Hawkeye()
	hulk = Hulk()
	heroes = pygame.sprite.Group()
	heroes.add(cap)
	heroes.add(widow)
	heroes.add(tony)
	heroes.add(thor)
	heroes.add(hawkeye)
	heroes.add(hulk)

def drag_and_drop():

	global money
	for h in heroes:
		if event.button == 1 and click[0] > h.rect.x and click[0] < h.rect.x + 40 and click[1] > h.rect.y and click[1] < h.rect.y + 50 and h.rect.x == h.x:
			h.moving = True
		elif event.button == 3 and not pygame.sprite.spritecollideany(h, decorations) and h.rect.x < 960 and h.rect.y < 760:
			h.moving = False
			money -= h.cost
		elif event.button == 3 and h.rect.x > 1000:
			h.moving = False
			h.rect.x = h.x
			h.rect.y = h.y

def draw_heroes():

	for h in heroes:
		if h.moving:
			h.place(click, money)
		if h.rect.x == h.x:
			BASICFONT = pygame.font.Font('freesansbold.ttf', 15)
			text = BASICFONT.render("$" + str(h.cost), 1, (255,255,0))
			text_rect = text.get_rect()
			text_rect.topleft = (h.x, h.y + h.rect.height + 5)
			DISPLAYSURF.blit(text, text_rect)
		DISPLAYSURF.blit(h.image, h.rect)

def round_1():

	global bots
	bots = pygame.sprite.Group()
	bots.add(Weak_Bot())
	bots.add(Blue_Bot())
	bots.add(Red_Bot())
	bots.add(Ultron())

def draw_bots():

	global lives
	for b in bots:
		if b.rect.x < 0:
			bots.remove(b)
			lives += b.health
		lives -= b.move(counter)
		DISPLAYSURF.blit(b.image, b.rect)

lives = 100
money = 500

images()
map_sprites()
hero_sprites()

counter = 0
while True:

	click = pygame.mouse.get_pos()
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			drag_and_drop()

	DISPLAYSURF.fill((255, 255, 255))
	draw_map()
	draw_heroes()
	draw_bots()
	pygame.display.update()
	fpsClock.tick(FPS)
	counter += 1
