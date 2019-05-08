import pygame
import sys
import math
pygame.init()

class Shield(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/shield.png')
        self.rect = pygame.Rect(x, y, 20, 20)
