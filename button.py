import pygame
import sys
pygame.init()

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, text, cost):

        super().__init__()
        self.image = pygame.image.load('resources/button(1).png')
        self.rect = pygame.Rect(x, y, 150, 300)
        self.text = text
        self.pressed = False
        self.cost = cost
