import pygame
import sys
pygame.init()

class Road(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('resources/road.jpg')
        self.rect = pygame.Rect(self.x, self.y, 1000, 50)
