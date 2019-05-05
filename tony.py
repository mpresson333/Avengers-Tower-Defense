import pygame
import sys
pygame.init()

class Tony(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1085
        self.y = 360
        self.image = pygame.image.load('resources/tony.png')
        self.rect = pygame.Rect(self.x, self.y, 30, 50)
        self.speed = 2
        self.range = 100
        self.cost = 300

    def place(self, coor, money):

        if money >= self.cost:
            self.rect.x = coor[0]
            self.rect.y = coor[1]
