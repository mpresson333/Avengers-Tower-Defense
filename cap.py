import pygame
import sys
from shield import Shield
import math
pygame.init()

class Cap(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1085
        self.y = 340
        self.image = pygame.image.load('resources/cap.png')
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.speed = 2
        self.range = 150
        self.cost = 450
        self.moving = False
        self.shield = Shield(self.rect.centerx + 1, self.rect.centery + 1)

    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]
