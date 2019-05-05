import pygame
import sys
pygame.init()

class Road(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/road.jpg')
        self.rect = pygame.Rect(x, y, 1000, 50)
