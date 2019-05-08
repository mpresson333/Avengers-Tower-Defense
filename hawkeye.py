import pygame
import sys
pygame.init()

class Hawkeye(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1090
        self.y = 225
        self.image = pygame.image.load('resources/hawkeye.png')
        self.rect = pygame.Rect(self.x, self.y, 30, 50)
        self.speed = 2
        self.range = 200
        self.cost = 450
        self.moving = False

    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]
