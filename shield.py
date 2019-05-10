import pygame
import sys
import math
pygame.init()

class Shield(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/shield.png')
        self.rect = pygame.Rect(x, y, 20, 20)
        self.out = True

    def throw(self, cap, b, bots):

        if self.out:
            self.rect.x -= cap.speed/len(bots)
        else:
            self.rect.x += cap.speed/len(bots)

        if cap.rect.x - self.rect.x > 160:
            self.out = False

        if pygame.sprite.collide_rect(self, b) and self.out:
            self.out = False
            if b.health >= cap.damage:
                b.health -= cap.damage
                return cap.damage
            else:
                b.health -= cap.health - 1
                return cap.health - 1
        elif pygame.sprite.collide_rect(self, b) and not self.out:
            self.rect.x = cap.rect.x
            self.rect.y = cap.rect.y
            if b.health >= cap.damage:
                b.health -= cap.damage
                return cap.damage
            else:
                b.health -= cap.damage - 1
                return cap.damage - 1

        else:
            return 0
