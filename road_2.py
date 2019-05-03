import pygame
import sys
pygame.init()

class Road_2(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('resources/road(2).jpg')
        self.rect = pygame.Rect(self.x, self.y, 50, 800)
