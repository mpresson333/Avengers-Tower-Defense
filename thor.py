import pygame
import sys
from button import Button
pygame.init()

class Thor(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1085
        self.y = 700
        self.image = pygame.image.load('resources/thor.png')
        self.rect = pygame.Rect(self.x, self.y, 40, 50)
        self.speed = 8
        self.range = 150
        self.cost = 1000
        self.moving = False
        self.hammer = None
        self.damage = 2
        self.direction = 0
        self.button_1 = Button(1025, 125, "Increase hammer speed by 50%", 300)
        self.button_2 = Button(1025, 475, "Double damage", 300)

    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]

    def change_image(self):

        if self.hammer == None:
            self.image = pygame.image.load('resources/thor.png')
        else:
            self.image = pygame.image.load('resources/thor(3).png')
