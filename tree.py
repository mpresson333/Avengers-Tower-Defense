import pygame
import sys
pygame.init()

class Tree(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/tree.png')
        self.rect = pygame.Rect(x, y, 50, 50)
