import pygame
import sys
pygame.init()

class Road_2(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/road(2).jpg')
        self.rect = pygame.Rect(x, y, 50, 800)
