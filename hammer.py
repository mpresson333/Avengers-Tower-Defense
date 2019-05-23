import pygame
import sys
pygame.init()

class Hammer(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = None
        self.rect = pygame.Rect(x, y, 15, 15)
        self.out = True

    #moves thor's hammer in a cardinal direction and checks for collisions with a bot
    def throw(self, thor, bots, DISPLAYSURF):

        if thor.direction == 1:
            self.image = self.image = pygame.image.load('resources/hammer(3).png')
            if self.out:
                self.rect.y -= thor.speed
            else:
                self.rect.y += thor.speed

            if thor.rect.y - self.rect.y >= thor.range:
                self.out = False

            if self.rect.y >= thor.rect.y:
                thor.hammer = None

        elif thor.direction == 2:
            self.image = pygame.image.load('resources/hammer.png')
            if self.out:
                self.rect.x -= thor.speed
            else:
                self.rect.x += thor.speed

            if thor.rect.x - self.rect.x >= thor.range:
                self.out = False

            if self.rect.x >= thor.rect.x:
                thor.hammer = None

        elif thor.direction == 3:
            self.image = pygame.image.load('resources/hammer(4).png')
            if self.out:
                self.rect.y += thor.speed
            else:
                self.rect.y -= thor.speed

            if self.rect.y - thor.rect.y >= thor.range:
                self.out = False

            if self.rect.y <= thor.rect.y:
                thor.hammer = None

        else:
            self.image = pygame.image.load('resources/hammer(2).png')
            if self.out:
                self.rect.x += thor.speed
            else:
                self.rect.x -= thor.speed

            if self.rect.x - thor.rect.x >= thor.range:
                self.out = False

            if self.rect.x <= thor.rect.x:
                thor.hammer = None

        if thor.hammer != None:
            DISPLAYSURF.blit(self.image, self.rect)

        b = pygame.sprite.spritecollideany(self, bots)
        if b != None:
            if self.out:
                self.out = False
                if b.health >= thor.damage:
                    b.health -= thor.damage
                    return thor.damage
                else:
                    r = b.health
                    b.health = 0
                    return r

            else:
                self.rect.x = thor.rect.x
                self.rect.y = thor.rect.y
                if b.health >= thor.damage:
                    b.health -= thor.damage
                    return thor.damage
                else:
                    r = b.health
                    b.health = 0
                    return r

        else:
            return 0
