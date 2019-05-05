import pygame
import sys
pygame.init()

class Box(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/box.png')
        self.rect = pygame.Rect(x, y, 50, 50)
