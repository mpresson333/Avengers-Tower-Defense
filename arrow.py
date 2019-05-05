import pygame
import sys
pygame.init()

class Arrow(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/arrow.png')
        self.rect = pygame.Rect(x, y, 100, 50)
