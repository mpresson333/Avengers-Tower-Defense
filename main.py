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
import math
from shield import Shield
from hammer import Hammer
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
	global widow
	global cap
	global tony
	global thor
	global hawkeye
	global hulk
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
		if event.button == 1 and click[0] > h.rect.x and click[0] < h.rect.x + 40 and click[1] > h.rect.y and click[1] < h.rect.y + 50 and h.rect.x == h.x and money >= h.cost:
			h.moving = True
		elif event.button == 3 and not pygame.sprite.spritecollideany(h, decorations) and h.rect.x < 960 and h.rect.y < 760 and h.moving:
			h.moving = False
			money -= h.cost
		elif event.button == 3 and h.rect.x > 1000 and h.moving:
			h.moving = False
			h.rect.x = h.x
			h.rect.y = h.y

def draw_heroes():

	for h in heroes:
		if h.moving:
			h.place(click)
		if h.rect.x == h.x and not h.moving:
			BASICFONT = pygame.font.Font('freesansbold.ttf', 15)
			text = BASICFONT.render("$" + str(h.cost), 1, (255,255,0))
			text_rect = text.get_rect()
			text_rect.topleft = (h.x, h.y + h.rect.height + 5)
			DISPLAYSURF.blit(text, text_rect)
		DISPLAYSURF.blit(h.image, h.rect)

def round_1():

	global bots
	bots = pygame.sprite.Group()
	for x in range(50):
		bots.add(Weak_Bot(1000 + 10*x))

def draw_bots():

	global lives
	for b in bots:
		if b.rect.x < 0:
			b.kill()
			lives += b.health
		if b.health <= 0:
			b.kill()
		lives -= b.move(counter)
		if b.rect.x < 985:
			DISPLAYSURF.blit(b.image, b.rect)

def direction(c, p):

	if p.rect.centerx >= c.rect.centerx - math.sqrt((c.rect.centerx - p.rect.centerx)**2 + (c.rect.centery - p.rect.centery)**2)/math.sqrt(2):
	    if p.rect.centerx >= c.rect.centerx + math.sqrt((c.rect.centerx - p.rect.centerx)**2 + (c.rect.centery - p.rect.centery)**2)/math.sqrt(2):
	        return 4
	    else:
	        if p.rect.centery < c.rect.centery:
	            return 1
	        else:
	            return 3
	else:
	    return 2

def widow_attack(b, widow, counter, FPS):

	global money
	if widow.range >= math.sqrt((widow.rect.centerx - b.rect.centerx)**2 + (widow.rect.centery - b.rect.centery)**2) and widow.rect.x != widow.x and not widow.moving and counter >= widow.last + (FPS/widow.speed):
		money += widow.shoot(b, counter, FPS)
	widow.change_image(b, counter)

def cap_attack(bots, cap):

	global money
	for b in bots:
		if cap.range >= math.sqrt((cap.rect.centerx - b.rect.centerx)**2 + (cap.rect.centery - b.rect.centery)**2) and cap.rect.x != cap.x and not cap.moving and cap.shield == None:
			cap.shield = Shield(cap.rect.x, cap.rect.y)

	if cap.shield != None:
		money += cap.shield.throw(cap, bots)
		DISPLAYSURF.blit(cap.shield.image, cap.shield.rect)
		if cap.rect.x <= cap.shield.rect.x:
			cap.shield = None

	cap.change_image()

def hawkeye_attack(b, hawkeye, counter, FPS):

	global money
	if hawkeye.range >= math.sqrt((hawkeye.rect.centerx - b.rect.centerx)**2 + (hawkeye.rect.centery - b.rect.centery)**2) and hawkeye.rect.x != hawkeye.x and not hawkeye.moving and counter >= hawkeye.last + (FPS/hawkeye.speed):
		money += hawkeye.shoot(b, counter, FPS)
	hawkeye.change_image(b, counter)

def tony_attack(b, tony, counter, FPS):

	global money
	if tony.range >= math.sqrt((tony.rect.centerx - b.rect.centerx)**2 + (tony.rect.centery - b.rect.centery)**2) and tony.rect.x != tony.x and not tony.moving and counter >= tony.last + (FPS/tony.speed):
		money += tony.shoot(b, counter, FPS)
	tony.change_image(b, counter)

def thor_attack(bots, thor):

	global money
	for b in bots:
		if thor.range >= math.sqrt((thor.rect.centerx - b.rect.centerx)**2 + (thor.rect.centery - b.rect.centery)**2) and thor.rect.x != thor.x and not thor.moving and thor.hammer == None:
			thor.hammer = Hammer(thor.rect.x, thor.rect.y)
			d = direction(thor, b)

	if thor.hammer != None:
		money += thor.hammer.throw(thor, bots, d)
		DISPLAYSURF.blit(thor.hammer.image, thor.hammer.rect)
		if thor.rect.x <= thor.hammer.rect.x:
			thor.hammer = None

	thor.change_image()

def hulk_attack(b, hulk, counter, FPS):

	global money
	if hulk.range >= math.sqrt((hulk.rect.centerx - b.rect.centerx)**2 + (hulk.rect.centery - b.rect.centery)**2) and hulk.rect.x != hulk.x and not hulk.moving:
		money += hulk.smash(b, counter, FPS)
	hulk.change_image(b, counter)

def avengers_assemble(bots, widow, cap, hawkeye, tony, thor, hulk, counter, FPS):

	for b in bots:
		if b.rect.x <= 1000:
			widow_attack(b, widow, counter, FPS)
			hawkeye_attack(b, hawkeye, counter, FPS)
			tony_attack(b, tony, counter, FPS)
			hulk_attack(b, hulk, counter, FPS)

	cap_attack(bots, cap)
	thor_attack(bots, thor)

lives = 100
money = 1000

images()
map_sprites()
hero_sprites()
round_1()

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
	avengers_assemble(bots, widow, cap, hawkeye, tony, thor, hulk, counter, FPS)
	pygame.display.update()
	fpsClock.tick(FPS)
	counter += 1
