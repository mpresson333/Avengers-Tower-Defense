import pygame
import sys
import math
from button import Button
pygame.init()

class Hawkeye(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1090
        self.y = 225
        self.image = pygame.image.load('resources/hawkeye.png')
        self.rect = pygame.Rect(self.x, self.y, 30, 50)
        self.speed = 2
        self.range = 800
        self.cost = 450
        self.moving = False
        self.damage = 1
        self.last = 0
        self.button_1 = Button(1025, 125, "Increase attack speed by 50%", 300)
        self.button_2 = Button(1025, 475, "Double damage", 300)

    #moves the sprite with the mouse
    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]

    #uses an attacking attribute to allow hawkeye to shoot bots
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

    #changes hawkeye's image
    def change_image(self, b, counter):

        if self.range >= math.sqrt(((self.rect.centerx - b.rect.centerx)**2) + ((self.rect.centery - b.rect.centery)**2)) and self.rect.x != self.x and not self.moving:
            if b.rect.centerx <= self.rect.centerx:
                self.image = pygame.image.load('resources/hawkeye(2.2).png')
            else:
                self.image = pygame.image.load('resources/hawkeye(2.1).png')
        elif counter % 45 == 0:
            self.image = pygame.image.load('resources/hawkeye.png')
