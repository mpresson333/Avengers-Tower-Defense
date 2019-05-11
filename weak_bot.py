import pygame
import sys
pygame.init()

class Weak_Bot(pygame.sprite.Sprite):

    def __init__(self, x):

        super().__init__()
        self.image = pygame.image.load('resources/ultron(1.1).png')
        self.rect = pygame.Rect(x, 80, 30, 40)
        self.health = 1
        self.speed = 2

    def move(self, counter):

        if self.rect.x > 156 and self.rect.y < 86:
            self.rect.x -= self.speed
            if counter % 31 == 0:
                self.rect.y += 5
            elif counter % 31 == 15:
                self.rect.y -= 5

        elif self.rect.y < 380 and self.rect.x < 166:
            self.rect.y += self.speed
            self.image = pygame.image.load('resources/ultron(1.2).png')
            if counter % 31 == 0:
                self.rect.x += 5
            elif counter % 31 == 15:
                self.rect.x -= 5

        elif self.rect.x < 755 and self.rect.y < 387:
            self.rect.x += self.speed
            if counter % 31 == 0:
                self.rect.y += 5
            elif counter % 31 == 15:
                self.rect.y -= 5

        elif self.rect.y < 680 and self.rect.x > 746:
            self.rect.y += self.speed
            self.image = pygame.image.load('resources/ultron(1.1).png')
            if counter % 31 == 0:
                self.rect.x += 5
            elif counter % 31 == 15:
                self.rect.x -= 5

        else:
            self.rect.x -= self.speed
            if counter % 31 == 0:
                self.rect.y += 5
            elif counter % 31 == 15:
                self.rect.y -= 5

        if self.rect.x < 0:
            return self.health
            self.kill()
        else:
            return 0
