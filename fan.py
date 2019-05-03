import pygame
import sys
pygame.init()

class Fan(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('resources/fan.png')
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
