import pygame
import sys
pygame.init()

class Blue_Bot(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.x = 1000
        self.y = 80
        self.image = pygame.image.load('resources/ultron(2.2.1).png')
        self.rect = pygame.Rect(self.x, self.y, 30, 40)
        self.health = 2

    def move(self, counter):

        if self.rect.x > 156 and self.rect.y < 86:
            self.rect.x -= 4
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(2.2.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(2.2.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(2.2.1).png')

        elif self.rect.y < 380 and self.rect.x < 166:
            self.rect.y += 4
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(2.1.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(2.1.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(2.1.1).png')

        elif self.rect.x < 755 and self.rect.y < 387:
            self.rect.x += 4
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(2.1.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(2.1.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(2.1.1).png')

        elif self.rect.y < 680 and self.rect.x > 746:
            self.rect.y += 4
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(2.2.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(2.2.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(2.2.1).png')

        else:
            self.rect.x -= 4
            if counter % 15 == 0:
                self.image = pygame.image.load('resources/ultron(2.2.2).png')
            elif counter % 15 == 5:
                self.image = pygame.image.load('resources/ultron(2.2.3).png')
            elif counter % 15 == 10:
                self.image = pygame.image.load('resources/ultron(2.2.1).png')

        if self.rect.x < 0:
            return True
            self.kill()
        else:
            return False
