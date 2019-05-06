import pygame
import sys
pygame.init()

class Hulk(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1085
        self.y = 580
        self.image = pygame.image.load('resources/hulk.png')
        self.rect = pygame.Rect(self.x, self.y, 50, 60)
        self.speed = 1
        self.range = 75
        self.cost = 600
        self.moving = False

    def place(self, coor, money):

        if money >= self.cost and self.moving:
            self.rect.x = coor[0]
            self.rect.y = coor[1]
