import pygame
import sys
pygame.init()

class Tower(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('resources/tower.png')
        self.rect = pygame.Rect(self.x, self.y, 50, 100)
