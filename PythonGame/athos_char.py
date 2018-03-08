import pygame
from pygame.locals import *


class Athos(pygame.sprite.Sprite):

    athos_animated = []
    overworld = []

    HP = 30
    attack = 25

    i = 0
    x = -300
    y = 310

    left_i = 3
    down_i = 7
    up_i = 11
    right_i = 15

    buffer = False

    dummy_var = 0
    o_i = 0
    o_x = -60
    o_y = 216

    change_x = 0
    change_y = 0

    alpha_val = 255
    plus = True

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load('aths.png').convert()
        self.image.set_colorkey((128, 160, 128), RLEACCEL)

        self.image.set_clip(188, 11, 95, 76)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.athos_animated.append(draw_me)

        self.image.set_clip(80, 11, 95, 76)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.athos_animated.append(draw_me)

        self.image.set_clip(183, 94, 95, 76)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.athos_animated.append(draw_me)

        self.image2 = pygame.image.load('athsglas.png').convert()
        self.image2.set_colorkey((128, 160, 128), RLEACCEL)

        self.image2.set_clip(188, 11, 95, 76)
        draw_me = self.image2.subsurface(self.image2.get_clip())
        self.athos_animated.append(draw_me)

        self.image2.set_clip(80, 11, 95, 76)
        draw_me = self.image2.subsurface(self.image2.get_clip())
        self.athos_animated.append(draw_me)

        self.image2.set_clip(183, 94, 95, 76)
        draw_me = self.image2.subsurface(self.image2.get_clip())
        self.athos_animated.append(draw_me)

        self.image3 = pygame.image.load('athsglas2.png').convert()
        self.image3.set_colorkey((128, 160, 128), RLEACCEL)

        self.image3.set_clip(10, 11, 95, 76)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.athos_animated.append(draw_me)

        self.image3.set_clip(118, 11, 95, 76)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.athos_animated.append(draw_me)

        self.image3.set_clip(15, 94, 95, 76)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.athos_animated.append(draw_me)

        self.image3 = pygame.image.load('archsage.png').convert()
        self.image3.set_colorkey((128, 160, 128), RLEACCEL)

        self.image3.set_clip(5, 29, 16, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(25, 29, 16, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(45, 29, 16, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(12, 132, 18, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(44, 132, 19, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(76, 132, 18, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(108, 132, 17, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(12, 164, 17, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(44, 164, 17, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(76, 164, 17, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(108, 164, 17, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(12, 196, 16, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(44, 196, 16, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(76, 196, 16, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(108, 196, 16, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(12, 228, 18, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(44, 228, 19, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(76, 228, 18, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image3.set_clip(108, 228, 17, 18)
        draw_me = self.image3.subsurface(self.image3.get_clip())
        self.overworld.append(draw_me)

        self.image = self.athos_animated[0]

        self.rect = self.image.get_rect()

    def update(self, x, SCREEN):
        num = x

        initial = self.athos_animated[0]

        if num is 6:
            if self.x != 20:
                self.x += 10
                SCREEN.blit(pygame.transform.scale(initial, (285, 228)), (self.x, self.y))
            else:
                SCREEN.blit(pygame.transform.scale(initial, (285, 228)), (self.x, self.y))
        elif num is 7 or num is 9 or num is 11:
            self.image = self.athos_animated[self.i]
            SCREEN.blit(pygame.transform.scale(self.image, (285, 228)), (self.x, self.y))
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
                self.plus = True
                initial.set_alpha(self.alpha_val)
                SCREEN.blit(pygame.transform.scale(initial, (285, 228)), (self.x, self.y))
                self.alpha_val -= 5
        elif num is 17:
            self.i = 6
            initial.set_alpha(self.alpha_val)
            if self.x != 600:
                self.x -= 10
                SCREEN.blit(pygame.transform.scale(self.athos_animated[self.i], (285, 228)), (self.x, self.y))
            else:
                SCREEN.blit(pygame.transform.scale(self.athos_animated[self.i], (285, 228)), (self.x, self.y))
        elif num is 18:
            self.image = self.athos_animated[self.i]
            SCREEN.blit(pygame.transform.scale(self.image, (285, 228)), (self.x, self.y))
            if self.i <= 8 and self.plus is True:
                self.i += 1
                if self.i is 9:
                    self.plus = False
                    self.i -= 2
            elif self.plus is False and self.i >= 6:
                self.i -= 1
                if self.i is 5:
                    self.i += 2
                    self.plus = True

        elif num is 22:
            if self.alpha_val is 0:
                pass
            else:
                self.athos_animated[self.i].set_alpha(self.alpha_val)
                SCREEN.blit(pygame.transform.scale(self.athos_animated[self.i], (285, 228)), (self.x, self.y))
                self.alpha_val -= 5
        elif num is 30:
            self.plus = True
            if self.o_x != 6:
                self.o_x += 6
                SCREEN.blit(pygame.transform.scale(self.overworld[self.right_i], (80, 70)), (self.o_x, self.o_y))
                self.right_i += 1
                if self.right_i == 19:
                    self.right_i = 15
            else:
                SCREEN.blit(pygame.transform.scale(self.overworld[0], (80, 70)), (self.o_x, self.o_y))
        elif num is 31 or num is 32 or num is 33 or num is 60:
            SCREEN.blit(pygame.transform.scale(self.overworld[self.o_i], (80, 70)), (self.o_x, self.o_y))
            if self.o_i <= 2 and self.plus is True and self.buffer is False:
                self.o_i += 1
            elif self.o_i == 3 and self.plus is True and self.buffer is False:
                self.buffer = True
            elif self.o_i == 3 and self.plus is True and self.buffer is True and self.dummy_var != 3:
                self.dummy_var += 1
                SCREEN.blit(pygame.transform.scale(self.overworld[2], (80, 70)), (self.o_x, self.o_y))
            elif self.o_i == 3 and self.plus is True and self.buffer is True and self.dummy_var == 3:
                self.buffer = False
                self.dummy_var = 0
                self.plus = False
                self.o_i -= 2
            elif self.plus is False and self.o_i >= 0:
                self.o_i -= 1
                if self.o_i is -1:
                    self.o_i += 2
                    self.plus = True
        elif num is 61:
            if self.o_x != self.change_x:
                if self.o_x < self.change_x:
                    SCREEN.blit(pygame.transform.scale(self.overworld[self.right_i], (90, 70)), (self.o_x, self.o_y))
                    self.right_i += 1
                    if self.right_i == 19:
                        self.right_i = 15
                    self.o_x += 1
                else:
                    SCREEN.blit(pygame.transform.scale(self.overworld[self.left_i], (90, 70)), (self.o_x, self.o_y))
                    self.left_i += 1
                    if self.left_i == 10:
                        self.left_i = 6
                    self.o_x -= 1
            elif self.o_y != self.change_y:
                if self.o_y < self.change_y:
                    SCREEN.blit(pygame.transform.scale(self.overworld[self.down_i], (90, 70)), (self.o_x, self.o_y))
                    self.down_i += 1
                    if self.down_i == 10:
                        self.down_i = 7
                    self.o_y += 1
                else:
                    SCREEN.blit(pygame.transform.scale(self.overworld[self.up_i], (90, 70)), (self.o_x, self.o_y))
                    self.up_i += 1
                    if self.up_i == 15:
                        self.up_i = 11
                    self.o_y -= 1
        elif num is 100:
            SCREEN.blit(pygame.transform.scale(self.athos_animated[7], (285, 228)), (400, 300))

        elif num > 18:
            SCREEN.blit(pygame.transform.scale(self.athos_animated[self.i], (285, 228)), (self.x, self.y))

        else:
            SCREEN.blit(pygame.transform.scale(initial, (285, 228)), (self.x, self.y))
