import pygame
import sys
from button import Button
pygame.init()

class Cap(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1085
        self.y = 340
        self.image = pygame.image.load('resources/cap.png')
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.speed = 5
        self.range = 150
        self.cost = 450
        self.moving = False
        self.shield = None
        self.damage = 1
        self.direction = 0
        self.button_1 = Button(1025, 125, "Increase shield speed by 60%", 300)
        self.button_2 = Button(1025, 475, "Double damage", 300)

    def place(self, coor):

        self.rect.x = coor[0]
        self.rect.y = coor[1]

    def change_image(self):

        if self.shield == None:
            self.image = pygame.image.load('resources/cap.png')
        else:
            if self.shield.rect.x > self.rect.x or self.shield.rect.y > self.rect.y:
                self.image = pygame.image.load('resources/cap(2.2).png')
            else:
                self.image = pygame.image.load('resources/cap(2.1).png')
