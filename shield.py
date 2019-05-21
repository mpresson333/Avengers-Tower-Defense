import pygame
import sys
pygame.init()

class Shield(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load('resources/shield.png')
        self.rect = pygame.Rect(x, y, 20, 20)
        self.out = True

    def throw(self, cap, bots, DISPLAYSURF):

        if cap.direction== 1:
            if self.out:
                self.rect.y -= cap.speed
            else:
                self.rect.y += cap.speed

            if cap.rect.y - self.rect.y >= cap.range:
                self.out = False

            if self.rect.y >= cap.rect.y:
                cap.shield = None

        elif cap.direction== 2:
            if self.out:
                self.rect.x -= cap.speed
            else:
                self.rect.x += cap.speed

            if cap.rect.x - self.rect.x >= cap.range:
                self.out = False

            if self.rect.x >= cap.rect.x:
                cap.shield = None

        elif cap.direction== 3:
            if self.out:
                self.rect.y += cap.speed
            else:
                self.rect.y -= cap.speed

            if self.rect.y - cap.rect.y >= cap.range:
                self.out = False

            if self.rect.y <= cap.rect.y:
                cap.shield = None

        else:
            if self.out:
                self.rect.x += cap.speed
            else:
                self.rect.x -= cap.speed

            if self.rect.x - cap.rect.x >= cap.range:
                self.out = False

            if self.rect.x <= cap.rect.x:
                cap.shield = None

        if cap.shield != None:
            DISPLAYSURF.blit(self.image, self.rect)

        b = pygame.sprite.spritecollideany(self, bots)
        if b != None:
            if self.out:
                self.out = False
                if b.health >= cap.damage:
                    b.health -= cap.damage
                    return cap.damage
                else:
                    r = b.health
                    b.health = 0
                    return r

            else:
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
