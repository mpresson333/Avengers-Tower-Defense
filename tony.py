import pygame
import sys
pygame.init()

class Tony(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1095
        self.y = 460
        self.image = pygame.image.load('resources/tony.png')
        self.rect = pygame.Rect(self.x, self.y, 30, 50)
        self.speed = 2
        self.range = 100
        self.cost = 450
        self.moving = False

    def place(self, coor, money):

        if money >= self.cost:
            self.rect.x = coor[0]
            self.rect.y = coor[1]
