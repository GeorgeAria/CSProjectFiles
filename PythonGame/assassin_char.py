
import pygame
from pygame.locals import *


class Assassin(pygame.sprite.Sprite):

    girl_animated = []
    i = 1;
    si = 600

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load('assassin.png').convert()
        self.image.set_colorkey((112, 154, 209), RLEACCEL)

        self.image.set_clip(12, 10, 24, 36)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(41, 9, 22, 36)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(70, 9, 23, 35)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(100, 11, 24, 33)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(131, 15, 39, 28)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(176, 14, 39, 28)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(224, 6, 29, 31)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(259, 5, 26, 31)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(293, 4, 27, 32)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(327, 5, 35, 31)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(368, 6, 60, 34)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(436, 6, 34, 32)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(44, 52, 30, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(80, 53, 27, 28)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(117, 52, 28, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(151, 52, 31, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(190, 52, 25, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(224, 52, 30, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(260, 52, 30, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(296, 53, 30, 34)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(331, 58, 29, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(367, 59, 30, 28)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(405, 57, 31, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(443, 56, 31, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(6, 104, 28, 29)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(41, 99, 30, 32)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(76, 98, 30, 26)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(112, 98, 38, 32)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(159, 94, 26, 35)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(192, 95, 28, 33)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(228, 94, 28, 35)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(263, 92, 23, 37)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(294, 92, 31, 37)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(332, 92, 29, 37)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(368, 92, 26, 37)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)
        self.image.set_clip(406, 94, 24, 36)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.girl_animated.append(draw_me)

        self.image = self.girl_animated[0]

        self.rect = self.image.get_rect()

    def update(self, SCREEN):

        self.image = self.girl_animated[self.i]
        if self.i >= 5 and self.i <= 25:
            self.si = 550
            SCREEN.blit(self.image, (self.si, 400))
        elif self.i >= 26 and self.i <= 36:
            self.si += 10
            if self.si > 600:
                SCREEN.blit(self.image, (600, 400))
            else:
                SCREEN.blit(self.image, (self.si, 400))
        else:
            self.si = 600
            SCREEN.blit(self.image, (self.si, 400))
        self.i += 1;
        if self.i is len(self.girl_animated):
            self.i = 0
