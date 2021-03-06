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
pygame.mixer.music.load('resources/Avengers Suite (Theme).mp3')
pygame.mixer.music.play(-1, 0.0)

#just loads all images from my resources folder into the game
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

#creates all sprites for the decorations in the game, with hitboxes, and adds them all to a sprite group
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

#draws all non-sprite images into the screen and adds the round and lives indicators
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
	text = BASICFONT.render("Round " + str(round), 1, (0,0,0))
	text_rect.topleft = (900, 775)
	DISPLAYSURF.blit(text, text_rect)

#creates all the hero sprites and adds them to a sprite group
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

#allows the player to click and drag a hero and drop them with a right click. heroes cannot be dropped on decorations or the menu
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

#draws all hero sprites and moves them if they are being dragged... also displays cost if they are in the menu
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

#draws all the enemies, as well as killing them if they reach the end or run out of health, and affects the player's lives accordingly
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

#finds the relative cardinal direction between two sprites, used for cap and thor's projectiles
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

#allows black widow to shoot a bot one at a time at a certain rate if the bot is in range, and adds money to the player's bank
def widow_attack(b, widow, counter, FPS):

	global money
	if widow.range >= math.sqrt((widow.rect.centerx - b.rect.centerx)**2 + (widow.rect.centery - b.rect.centery)**2) and widow.rect.x != widow.x and not widow.moving and counter >= widow.last + (FPS/widow.speed):
		money += widow.shoot(b, counter, FPS)
	widow.change_image(b, counter)

#allows cap to throw his shield in a cardinal direction if a bot is within range, and adds money to the player's bank
def cap_attack(bots, cap):

	global money
	for b in bots:
		if cap.range >= math.sqrt((cap.rect.centerx - b.rect.centerx)**2 + (cap.rect.centery - b.rect.centery)**2) and cap.rect.x != cap.x and not cap.moving and cap.shield == None:
			cap.shield = Shield(cap.rect.x, cap.rect.y)
			cap.direction = direction(cap, b)

	if cap.shield != None:
		money += cap.shield.throw(cap, bots, DISPLAYSURF)

	cap.change_image()

#allows hawkeye to shoot a bot one at a time at a certain rate if the bot is in range, and adds money to the player's bank
def hawkeye_attack(b, hawkeye, counter, FPS):

	global money
	if hawkeye.range >= math.sqrt((hawkeye.rect.centerx - b.rect.centerx)**2 + (hawkeye.rect.centery - b.rect.centery)**2) and hawkeye.rect.x != hawkeye.x and not hawkeye.moving and counter >= hawkeye.last + (FPS/hawkeye.speed):
		money += hawkeye.shoot(b, counter, FPS)
	hawkeye.change_image(b, counter)

#allows iron man to shoot a bot one at a time at a certain rate if the bot is in range, and adds money to the player's bank
def tony_attack(b, tony, counter, FPS):

	global money
	if tony.range >= math.sqrt((tony.rect.centerx - b.rect.centerx)**2 + (tony.rect.centery - b.rect.centery)**2) and tony.rect.x != tony.x and not tony.moving and counter >= tony.last + (FPS/tony.speed):
		money += tony.shoot(b, counter, FPS)
	tony.change_image(b, counter)

#allows thor to throw his hammer in a cardinal direction if a bot is within range, and adds money to the player's bank
def thor_attack(bots, thor):

	global money
	for b in bots:
		if thor.range >= math.sqrt((thor.rect.centerx - b.rect.centerx)**2 + (thor.rect.centery - b.rect.centery)**2) and thor.rect.x != thor.x and not thor.moving and thor.hammer == None:
			thor.hammer = Hammer(thor.rect.x, thor.rect.y)
			thor.direction = direction(thor, b)

	if thor.hammer != None:
		money += thor.hammer.throw(thor, bots, DISPLAYSURF)

	thor.change_image()

#allows hulk to smash all enemies within range at a slow rate
def hulk_attack(b, hulk, counter, FPS):

	global money
	if hulk.range >= math.sqrt((hulk.rect.centerx - b.rect.centerx)**2 + (hulk.rect.centery - b.rect.centery)**2) and hulk.rect.x != hulk.x and not hulk.moving:
		money += hulk.smash(b, counter, FPS)
	hulk.change_image(b, counter)

#runs the heroes's attack functions, upgrades them, and resets their image every round
def avengers_assemble(bots, widow, cap, hawkeye, tony, thor, hulk, counter, FPS):

	for b in bots:
		if b.rect.x <= 1000:
			widow_attack(b, widow, counter, FPS)
			hawkeye_attack(b, hawkeye, counter, FPS)
			tony_attack(b, tony, counter, FPS)
			hulk_attack(b, hulk, counter, FPS)

	cap_attack(bots, cap)
	thor_attack(bots, thor)

	if widow.button_1.pressed:
		widow.damage = 2
	if widow.button_2.pressed:
		widow.range = 225

	if cap.button_1.pressed:
		cap.speed = 12
	if cap.button_2.pressed:
		cap.damage = 2

	if hawkeye.button_1.pressed:
		hawkeye.speed = 3
	if hawkeye.button_2.pressed:
		hawkeye.damage = 2

	if hulk.button_1.pressed:
		hulk.range = 150
	if hulk.button_2.pressed:
		hulk.speed = 2

	if thor.button_1.pressed:
		thor.speed = 15
	if thor.button_2.pressed:
		thor.damage = 4

	if tony.button_1.pressed:
		tony.speed = 4
	if tony.button_2.pressed:
		tony.range = 225

	if len(bots) == 0:
		hawkeye.image = pygame.image.load('resources/hawkeye.png')
		hulk.image = pygame.image.load('resources/hulk.png')
		tony.image = pygame.image.load('resources/tony.png')
		widow.image = pygame.image.load('resources/widow.png')

#allows the player to click on a hero, which brings up an upgrade menu with buttons that, when clicked, upgrade a hero and take money from the player
def upgrade():

	global upgrading
	global hero
	global money
	for h in heroes:

		if upgrading and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click[0] > h.button_1.rect.x and click[0] < h.button_1.rect.x + 150 and click[1] > h.button_1.rect.y and click[1] < h.button_1.rect.y + 300 and h.rect.x != h.x and money >= h.button_1.cost and h == hero and not h.button_1.pressed:
			h.button_1.pressed = True
			money -= h.button_1.cost
			h.button_1.image = pygame.image.load('resources/button(2).png')

		if upgrading and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click[0] > h.button_2.rect.x and click[0] < h.button_2.rect.x + 150 and click[1] > h.button_2.rect.y and click[1] < h.button_2.rect.y + 300 and h.rect.x != h.x and money >= h.button_2.cost and h == hero and not h.button_2.pressed:
			h.button_2.pressed = True
			money -= h.button_1.cost
			h.button_2.image = pygame.image.load('resources/button(2).png')

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click2[0] > h.rect.x and click2[0] < h.rect.x + 30 and click2[1] > h.rect.y and click2[1] < h.rect.y + 50 and h.rect.x != h.x and not h.moving:
			upgrading = True
			hero = h

		if upgrading and hero != None:
			pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (1000, 100, 1200, 800))
			DISPLAYSURF.blit(hero.button_1.image, hero.button_1.rect)
			DISPLAYSURF.blit(hero.button_2.image, hero.button_2.rect)
			BASICFONT = pygame.font.Font('freesansbold.ttf', 10)
			text = BASICFONT.render(hero.button_1.text, 1, (0,0,0))
			text_rect = text.get_rect()
			text_rect.topleft = (1040, 270)
			DISPLAYSURF.blit(text, text_rect)
			text = BASICFONT.render(hero.button_2.text, 1, (0,0,0))
			text_rect.topleft = (1040, 620)
			DISPLAYSURF.blit(text, text_rect)
			text = BASICFONT.render("$300", 1, (0,0,0))
			text_rect.topleft = (1085, 300)
			DISPLAYSURF.blit(text, text_rect)
			text = BASICFONT.render("$300", 1, (0,0,0))
			text_rect.topleft = (1085, 650)
			DISPLAYSURF.blit(text, text_rect)
			text = BASICFONT.render("Press escape to exit", 1, (0,0,0))
			text_rect.topleft = (1050, 100)
			DISPLAYSURF.blit(text, text_rect)

#runs through the list of rounds and adds all the bots for the round into a sprite group
def spawn_bots(round):

	for b in round_list[round - 1]:
		bots.add(b)

#defines all 10 rounds
def rounds():

	round_1 = []
	for x in range(20):
		round_1.append(Weak_Bot(1000 + 30*x))
	round_2 = []
	for x in range(35):
		round_2.append(Weak_Bot(1000 + 30*x))
	round_3 = []
	for x in range(25):
		round_3.append(Weak_Bot(1000 + 30*x))
	for x in range(25):
		round_3.append(Blue_Bot(1000 + 30*x))
	round_4 = []
	for x in range(35):
		round_4.append(Weak_Bot(1000 + 30*x))
	for x in range(18):
		round_4.append(Blue_Bot(1000 + 30*x))
	round_5 = []
	for x in range(5):
		round_5.append(Weak_Bot(1000 + 30*x))
	for x in range(27):
		round_5.append(Blue_Bot(1000 + 30*x))
	round_6 = []
	for x in range(15):
		round_6.append(Weak_Bot(1000 + 30*x))
	for x in range(15):
		round_6.append(Blue_Bot(1000 + 30*x))
	for x in range(4):
		round_6.append(Red_Bot(1000 + 30*x))
	round_7 = []
	for x in range(20):
		round_7.append(Weak_Bot(1000 + 30*x))
	for x in range(20):
		round_7.append(Blue_Bot(1000 + 30*x))
	for x in range(5):
		round_7.append(Red_Bot(1000 + 30*x))
	round_8 = []
	for x in range(10):
		round_8.append(Weak_Bot(1000 + 30*x))
	for x in range(20):
		round_8.append(Blue_Bot(1000 + 30*x))
	for x in range(14):
		round_8.append(Red_Bot(1000 + 30*x))
	round_9 = []
	for x in range(30):
		round_9.append(Red_Bot(1000 + 30*x))
	round_10 = []
	for x in range(102):
		round_10.append(Blue_Bot(1000 + 30*x))
	round_11 = []
	for x in range(6):
		round_11.append(Weak_Bot(1000 + 30*x))
	for x in range(12):
		round_11.append(Blue_Bot(1000 + 30*x))
	for x in range(12):
		round_11.append(Red_Bot(1000 + 30*x))
	for x in range(1):
		round_11.append(Ultron(1000 + 30*x))
	round_12 = []
	for x in range(15):
		round_12.append(Blue_Bot(1000 + 30*x))
	for x in range(10):
		round_12.append(Red_Bot(1000 + 30*x))
	for x in range(3):
		round_12.append(Ultron(1000 + 30*x))
	round_13 = []
	for x in range(50):
		round_13.append(Blue_Bot(1000 + 30*x))
	for x in range(23):
		round_13.append(Red_Bot(1000 + 30*x))
	round_14 = []
	for x in range(49):
		round_14.append(Weak_Bot(1000 + 30*x))
	for x in range(15):
		round_14.append(Blue_Bot(1000 + 30*x))
	for x in range(10):
		round_14.append(Red_Bot(1000 + 30*x))
	for x in range(4):
		round_14.append(Ultron(1000 + 30*x))
	round_15 = []
	for x in range(20):
		round_15.append(Weak_Bot(1000 + 30*x))
	for x in range(15):
		round_15.append(Blue_Bot(1000 + 30*x))
	for x in range(12):
		round_15.append(Red_Bot(1000 + 30*x))
	for x in range(8):
		round_15.append(Ultron(1000 + 30*x))
	round_16 = []
	for x in range(40):
		round_16.append(Red_Bot(1000 + 30*x))
	for x in range(4):
		round_16.append(Ultron(1000 + 30*x))
	round_17 = []
	for x in range(15):
		round_17.append(Ultron(1000 + 30*x))
	round_18 = []
	for x in range(80):
		round_18.append(Red_Bot(1000 + 30*x))
	round_19 = []
	for x in range(10):
		round_19.append(Red_Bot(1000 + 30*x))
	for x in range(15):
		round_19.append(Ultron(1000 + 30*x))
	round_20 = []
	for x in range(20):
		round_20.append(Ultron(1000 + 30*x))
	return round_1, round_2, round_3, round_4, round_5, round_6, round_7, round_8, round_9, round_10, round_11, round_12, round_13, round_14, round_15, round_16, round_17, round_18, round_19, round_20

#displays the win screen
def win_screen():

	DISPLAYSURF.fill((255, 255, 255))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 100)
	text = BASICFONT.render("YOU WIN!", 1, (0,0,0))
	text_rect = text.get_rect()
	text_rect.topleft = (400, 350)
	DISPLAYSURF.blit(text, text_rect)

#displays the game over screen
def lose_screen():

	DISPLAYSURF.fill((255, 255, 255))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 100)
	text = BASICFONT.render("YOU LOSE!", 1, (0,0,0))
	text_rect = text.get_rect()
	text_rect.topleft = (400, 350)
	DISPLAYSURF.blit(text, text_rect)

lives = 100
money = 500

images()
map_sprites()
hero_sprites()

counter = 0
upgrading = False
hero = None
round = 0
bots = pygame.sprite.Group()
round_list = rounds()

#beautifully stitches all above functions together
while True:


	click = pygame.mouse.get_pos()
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			click2 = pygame.mouse.get_pos()
			if not upgrading:
				drag_and_drop()

		#allows player to escape the upgrade menu or start anew round
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				upgrading = False
				hero = None
			elif event.key == pygame.K_SPACE and len(bots) == 0:
				round += 1
				money += 175
				if round <= len(round_list):
					spawn_bots(round)

	DISPLAYSURF.fill((255, 255, 255))
	draw_map()
	draw_heroes()
	draw_bots()
	upgrade()
	avengers_assemble(bots, widow, cap, hawkeye, tony, thor, hulk, counter, FPS)
	if round > 20:
		win_screen()
	if lives < 1:
		lose_screen()
	pygame.display.update()
	fpsClock.tick(FPS)
	counter += 1
