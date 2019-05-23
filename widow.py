import pygame
import sys
import math
from button import Button
pygame.init()

class Widow(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1090
        self.y = 120
        self.image = pygame.image.load('resources/widow.png')
        self.rect = pygame.Rect(self.x, self.y, 30, 50)
        self.speed = 3
        self.range = 150
        self.cost = 300
        self.moving = False
        self.attacking = False
        self.damage = 1
        self.last = 0
        self.button_1 = Button(1025, 125, "Double damage", 300)
        self.button_2 = Button(1025, 475, "Increase range by 50%", 300)

    #moves the sprite with the mouse
    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]

    #uses an attacking attribute to allow black widow to shoot bots
    def shoot(self, b, counter, FPS):

        if counter % (FPS/self.speed) == 0:
            self.last = counter
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

    #changes black widow's image
    def change_image(self, b, counter):

        if self.range >= math.sqrt(((self.rect.centerx - b.rect.centerx)**2) + ((self.rect.centery - b.rect.centery)**2)) and self.rect.x != self.x and not self.moving:
            self.image = pygame.image.load('resources/widow(2).png')
        elif counter % 45 == 0:
            self.image = pygame.image.load('resources/widow.png')
