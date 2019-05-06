import pygame
import sys
pygame.init()

class Ultron(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load('resources/ultron(4.2.1).png')
        self.rect = pygame.Rect(1000, 80, 30, 40)
        self.health = 8
        self.speed = 8

    def move(self, counter):

        if self.rect.x > 156 and self.rect.y < 86:
            self.rect.x -= self.speed
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(4.2.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(4.2.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(4.2.1).png')

        elif self.rect.y < 380 and self.rect.x < 166:
            self.rect.y += self.speed
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(4.1.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(4.1.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(4.1.1).png')

        elif self.rect.x < 755 and self.rect.y < 387:
            self.rect.x += self.speed
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(4.1.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(4.1.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(4.1.1).png')

        elif self.rect.y < 680 and self.rect.x > 746:
            self.rect.y += self.speed
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(4.2.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(4.2.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(4.2.1).png')

        else:
            self.rect.x -= self.speed
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(4.2.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(4.2.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(4.2.1).png')

        if self.rect.x < 0:
            return self.health
            self.kill()
        else:
            return 0
