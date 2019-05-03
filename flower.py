import pygame
import sys
pygame.init()

class Flower(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('resources/flower.png')
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
