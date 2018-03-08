import pygame
from pygame.locals import *


class Roy(pygame.sprite.Sprite):

    roy_animated = []
    overworld = []

    HP = 25
    attack = 10

    i = 1
    x = 1000
    y = 310

    left_i = 3
    down_i = 7
    up_i = 11
    right_i = 15

    plus = True
    buffer = False

    dummy_var = 0
    o_i = 0
    o_x = -60
    o_y = 4

    change_x = 0
    change_y = 0
    alpha_val = 255

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load('roy_face.png').convert()
        self.image.set_colorkey((161, 199, 150), RLEACCEL)

        self.image.set_clip(4, 1, 87, 76)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.roy_animated.append(draw_me)

        self.image.set_clip(114, 4, 25, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.roy_animated.append(draw_me)

        self.image.set_clip(114, 26, 25, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.roy_animated.append(draw_me)

        self.image.set_clip(114, 45, 25, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.roy_animated.append(draw_me)

        self.image.set_clip(115, 64, 25, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.roy_animated.append(draw_me)

        self.image.set_clip(114, 83, 25, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.roy_animated.append(draw_me)

        self.image.set_clip(114, 102, 25, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.roy_animated.append(draw_me)

        self.image.set_clip(86, 102, 25, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.roy_animated.append(draw_me)

        self.image = pygame.image.load('roy.png').convert()
        self.image.set_colorkey((128, 160, 128), RLEACCEL)

        self.image.set_clip(62, 31, 16, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(83, 31, 15, 16)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(101, 30, 16, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(6, 135, 22, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(37, 135, 25, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(70, 135, 23, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(101, 135, 22, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(8, 164, 19, 20)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(39, 166, 20, 18)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(71, 167, 20, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(104, 166, 20, 18)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(9, 198, 17, 18)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(40, 198, 19, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(72, 198, 18, 18)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(104, 198, 18, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(6, 231, 22, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(37, 231, 25, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(70, 231, 23, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image.set_clip(101, 231, 22, 17)
        draw_me = self.image.subsurface(self.image.get_clip())
        self.overworld.append(draw_me)

        self.image = self.roy_animated[0]

        self.rect = self.image.get_rect()

    def update(self, x, SCREEN):
        num = x
        initial = self.roy_animated[0]

        if num is 0:
            pass
        elif num is 1:
            if self.x != 600:
                self.x -= 10
                SCREEN.blit(pygame.transform.scale(initial, (261, 228)), (self.x, self.y))
            else:
                SCREEN.blit(pygame.transform.scale(initial, (261, 228)), (self.x, self.y))
        elif num is 2 or num is 5 or num is 8 or num is 10 or num is 12 or num is 21:
            self.image = self.roy_animated[self.i]
            x = pygame.transform.scale(self.image, (75, 48))
            SCREEN.blit(pygame.transform.scale(initial, (261, 228)), (self.x, self.y))
            SCREEN.blit(x, (self.x + 48, self.y + 107))
            self.i += 1
            if self.i > len(self.roy_animated) - 1:
                self.i = 1
        elif num is 13 or num is 22:
            if self.alpha_val is 0:
                pass
            else:
                initial.set_alpha(self.alpha_val)
                SCREEN.blit(pygame.transform.scale(initial, (261, 228)), (self.x, self.y))
                self.alpha_val -= 5
        elif num is 16:
            initial.set_alpha(self.alpha_val)
            if self.x != 400:
                self.x -= 10
                SCREEN.blit(pygame.transform.scale(initial, (261, 228)), (self.x, self.y))
            else:
                SCREEN.blit(pygame.transform.scale(initial, (261, 228)), (self.x, self.y))
        elif num is 30:
            if self.o_x != 6:
                self.o_x += 6
                SCREEN.blit(pygame.transform.scale(self.overworld[self.right_i], (90, 70)), (self.o_x, self.o_y))
                self.right_i += 1
                if self.right_i == 19:
                    self.right_i = 15
            else:
                SCREEN.blit(pygame.transform.scale(self.overworld[0], (70, 70)), (self.o_x, self.o_y))

        elif num is 31 or num is 32 or num is 33 or num is 61:
            SCREEN.blit(pygame.transform.scale(self.overworld[self.o_i], (70, 70)), (self.o_x, self.o_y))
            if self.o_i <= 2 and self.plus is True and self.buffer is False:
                self.o_i += 1
            elif self.o_i == 3 and self.plus is True and self.buffer is False:
                self.buffer = True
            elif self.o_i == 3 and self.plus is True and self.buffer is True and self.dummy_var != 3:
                self.dummy_var += 1
                SCREEN.blit(pygame.transform.scale(self.overworld[2], (70, 70)), (self.o_x, self.o_y))
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
                SCREEN.blit(pygame.transform.scale(self.overworld[0], (70, 70)), (self.o_x, self.o_y))
        elif num is 60:
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
                        self.up_i = 10
                    self.o_y -= 1



        else:
            SCREEN.blit(pygame.transform.scale(initial, (261, 228)), (self.x, self.y))
