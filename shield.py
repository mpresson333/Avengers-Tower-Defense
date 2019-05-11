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

    def throw(self, cap, bots):

        if self.out:
            self.rect.x -= cap.speed
        else:
            self.rect.x += cap.speed

        if cap.rect.x - self.rect.x >= 160:
            self.out = False

        for b in bots:
            if pygame.sprite.collide_rect(self, b) and self.out:
                self.out = False
                if b.health >= cap.damage:
                    b.health -= cap.damage
                    return cap.damage
                else:
                    r = b.health
                    b.health = 0
                    return r

            elif pygame.sprite.collide_rect(self, b) and not self.out:
                self.rect.x = cap.rect.x
                self.rect.y = cap.rect.y
                if b.health >= cap.damage:
                    b.health -= cap.damage
                    return cap.damage
                else:
                    r = b.health
                    b.health = 0
                    return r

            else:
                return 0
