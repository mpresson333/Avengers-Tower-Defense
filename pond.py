import pygame
import sys
pygame.init()

class Pond(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/water.png')
        self.rect = pygame.Rect(x, y, 120, 120)
