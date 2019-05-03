import pygame
import sys
pygame.init()

class Pond(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('resources/water.png')
        self.rect = pygame.Rect(self.x, self.y, 120, 120)
