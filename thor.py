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
        self.speed = 1
        self.range = 100
        self.cost = 1000
        self.moving = False

    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]
