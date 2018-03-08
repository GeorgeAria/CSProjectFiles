import pygame
from pygame.locals import *


class Natasha(pygame.sprite.Sprite):

    natasha_animated = []
    i = 0
    x = -250
    y = 310
    alpha_val = 255
    plus = True

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load('nata1.png').convert()
        self.image.set_colorkey((128, 160, 128), RLEACCEL)

        self.image.set_clip(183, 73, 62, 66)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.natasha_animated.append(draw_me)

        self.image.set_clip(101, 74, 62, 66)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.natasha_animated.append(draw_me)

        self.image.set_clip(19, 73, 62, 66)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.natasha_animated.append(draw_me)

        self.image = self.natasha_animated[0]

        self.rect = self.image.get_rect()

    def update(self, x, SCREEN):
        num = x

        initial = self.natasha_animated[0]

        if num is 3:
            if self.x != 320:
                self.x += 10
                SCREEN.blit(pygame.transform.scale(initial, (220, 228)), (self.x, self.y))
            else:
                SCREEN.blit(pygame.transform.scale(initial, (220, 228)), (self.x, self.y))
        elif num is 4:
            self.image = self.natasha_animated[self.i]
            SCREEN.blit(pygame.transform.scale(self.image, (220, 228)), (self.x, self.y))
            if self.i <= 2 and self.plus is True:
                self.i += 1
                if self.i is 3:
                    self.plus = False
                    self.i -= 2
            elif self.plus is False and self.i >= 0:
                self.i -= 1
                if self.i is -1:
                    self.i += 2
                    self.plus = True
        elif num is 13:
            if self.alpha_val is 0:
                pass
            else:
                initial.set_alpha(self.alpha_val)
                SCREEN.blit(pygame.transform.scale(initial, (220, 228)), (self.x, self.y))
                self.alpha_val -= 5
        else:
            SCREEN.blit(pygame.transform.scale(initial, (220, 228)), (self.x, self.y))
