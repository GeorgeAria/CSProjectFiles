import pygame
from pygame.locals import *


class Soldier(pygame.sprite.Sprite):

    soldier_animated = []
    overworld = []

    HP = 30
    attack = 8

    i = 0
    x = -300
    y = 310

    buffer = False

    dummy_var = 0
    o_i = 0
    o_x = 1000
    o_y = 322

    left_i = 3


    alpha_val = 255
    plus = True

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load('soldierred2.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)

        self.image.set_clip(205, 1, 93, 72)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.soldier_animated.append(draw_me)

        self.image.set_clip(107, 1, 93, 72)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.soldier_animated.append(draw_me)

        self.image.set_clip(6, 1, 93, 72)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.soldier_animated.append(draw_me)

        self.image = pygame.image.load('soldier.png').convert()
        self.image.set_colorkey((128, 160, 128), RLEACCEL)

        self.image.set_clip(5, 88, 19, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(28, 88, 20, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(53, 86, 20, 19)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(6, 132, 22, 18)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(39, 132, 21, 18)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(72, 132, 20, 18)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(103, 132, 21, 18)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image = self.soldier_animated[0]

        self.rect = self.image.get_rect()

    def update(self, x, SCREEN):
        num = x

        initial = self.soldier_animated[0]

        if num is 19:
            if self.x != 100:
                self.x += 10
                SCREEN.blit(pygame.transform.scale(initial, (279, 228)), (self.x, self.y))
            else:
                SCREEN.blit(pygame.transform.scale(initial, (279, 228)), (self.x, self.y))
        elif num is 20:
            self.image = self.soldier_animated[self.i]
            SCREEN.blit(pygame.transform.scale(self.image, (279, 228)), (self.x, self.y))
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
        elif num is 22:
            if self.alpha_val is 0:
                pass
            else:
                initial.set_alpha(self.alpha_val)
                SCREEN.blit(pygame.transform.scale(initial, (279, 228)), (self.x, self.y))
                self.alpha_val -= 5
        elif num is 30:
            self.plus = True
            if self.o_x != 744:
                self.o_x -= 6
                SCREEN.blit(pygame.transform.scale(self.overworld[self.left_i], (80, 70)), (self.o_x, self.o_y))
                self.left_i += 1
                if self.left_i == 7:
                    self.left_i = 3
            else:
                SCREEN.blit(pygame.transform.scale(self.overworld[0], (80, 70)), (self.o_x, self.o_y))
        elif num is 31 or num is 32 or num is 33 or num is 60 or num is 61:
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
        else:
            SCREEN.blit(pygame.transform.scale(initial, (279, 228)), (self.x, self.y))
