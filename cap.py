import pygame
import sys
import math
pygame.init()

class Cap(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1085
        self.y = 340
        self.image = pygame.image.load('resources/cap.png')
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.speed = 8
        self.range = 150
        self.cost = 450
        self.moving = False
        self.attacking = False
        self.shield = None
        self.damage = 2

    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]

    def change_image(self):

        if self.shield == None:
            self.image = pygame.image.load('resources/cap.png')
        else:
            self.image = pygame.image.load('resources/cap(2.1).png')
