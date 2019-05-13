import pygame
import sys
import math
pygame.init()

class Hammer(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/hammer.png')
        self.rect = pygame.Rect(x, y, 15, 15)
        self.out = True

    def throw(self, thor, bots, d):

        if d == 1:
            if self.out:
                self.rect.y -= thor.speed
            else:
                self.rect.y += thor.speed

            if thor.rect.y - self.rect.y >= 160:
                self.out = False

        elif d == 2:
            if self.out:
                self.rect.x -= thor.speed
            else:
                self.rect.x += thor.speed

            if thor.rect.x - self.rect.x >= 160:
                self.out = False

        elif d == 3:
            if self.out:
                self.rect.y += thor.speed
            else:
                self.rect.y -= thor.speed

            if self.rect.y - thor.rect.y >= 160:
                self.out = False

        elif d == 4:
            if self.out:
                self.rect.x += thor.speed
            else:
                self.rect.x -= thor.speed

            if self.rect.x - thor.rect.x >= 160:
                self.out = False

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
