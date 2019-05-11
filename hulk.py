import pygame
import sys
import math
pygame.init()

class Hulk(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1085
        self.y = 580
        self.image = pygame.image.load('resources/hulk.png')
        self.rect = pygame.Rect(self.x, self.y, 50, 60)
        self.speed = 1
        self.range = 100
        self.cost = 600
        self.moving = False
        self.damage = 3

    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]

    def smash(self, b, counter, FPS):

        if counter % (FPS/self.speed) == 0:
            self.attacking = True
        else:
            self.attacking = False

        if self.attacking:
            if b.health >= self.damage:
                b.health -= self.damage
                return self.damage
            else:
                r = b.health
                b.health = 0
                return r
        else:
            return 0

    def change_image(self, b, counter):

        if self.range >= math.sqrt(((self.rect.centerx - b.rect.centerx)**2) + ((self.rect.centery - b.rect.centery)**2)) and self.rect.x != self.x and not self.moving:
            self.image = pygame.image.load('resources/hulk(2).png')
        elif counter % 60 == 0:
            self.image = pygame.image.load('resources/hulk.png')
