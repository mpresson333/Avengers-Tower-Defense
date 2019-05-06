import pygame
import sys
pygame.init()

class Widow(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1090
        self.y = 120
        self.image = pygame.image.load('resources/widow.png')
        self.rect = pygame.Rect(self.x, self.y, 30, 50)
        self.speed = 4
        self.range = 100
        self.cost = 300
        self.moving = False

    def place(self, coor, money):

        self.rect.x = coor[0]
        self.rect.y = coor[1]
