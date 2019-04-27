import pyagme
import sys
pygame.intit()
DISPLAYSURF = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Hello World!")
DISPLAYSURF.fill((255, 255, 255))

while True:

	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

pygame.display.update() 
