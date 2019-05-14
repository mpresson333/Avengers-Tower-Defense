import pygame
import sys
pygame.init()

class Thor(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1085
        self.y = 700
        self.image = pygame.image.load('resources/thor.png')
        self.rect = pygame.Rect(self.x, self.y, 40, 50)
        self.speed = 12
        self.range = 150
        self.cost = 1000
        self.moving = False
        self.hammer = None
        self.damage = 3
        self.direction = 0

    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]

    def change_image(self):

        if self.hammer == None:
            self.image = pygame.image.load('resources/thor.png')
        else:
            self.image = pygame.image.load('resources/thor(3).png')
