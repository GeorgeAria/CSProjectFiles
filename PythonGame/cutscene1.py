import pygame
import sys
import time
from pygame.locals import *
from main_char import Roy
from athos_char import Athos
from natasha_char import Natasha
from soldier_char import Soldier
from battle import main3


def main2():
    pygame.init()
    pygame.mixer.init()

    window_size = (960, 539)
    SCREEN = pygame.display.set_mode(window_size)

    background = pygame.image.load('back2.png').convert()
    background.set_colorkey((0, 0, 0), RLEACCEL)
    desert_background = pygame.image.load('desertback.png').convert()
    desert_background.set_colorkey((0, 0, 0), RLEACCEL)
    text_bubble = pygame.image.load('textbubble.png').convert()
    text_bubble.set_colorkey((0, 0, 0), RLEACCEL)
    text_arrow = pygame.image.load('textarrow.png').convert()
    text_arrow.set_colorkey((255, 255, 255), RLEACCEL)
    line_1 = pygame.image.load('line_1.png').convert()
    line_2 = pygame.image.load('line_2.png').convert()
    line_3 = pygame.image.load('line_3.png').convert()
    line_4 = pygame.image.load('line_4.png').convert()
    line_5 = pygame.image.load('line_5.png').convert()
    line_6 = pygame.image.load('line_6.png').convert()
    line_7 = pygame.image.load('line_7.png').convert()
    line_8 = pygame.image.load('line_8.png').convert()
    line_9 = pygame.image.load('line_9.png').convert()
    line_9a = pygame.image.load('line_9a.png').convert()
    line_10 = pygame.image.load('line_10.png').convert()
    line_11 = pygame.image.load('line_11.png').convert()
    theme = pygame.mixer.Sound("firstroad.ogg")
    theme2 = pygame.mixer.Sound("uhoh.ogg")


    rect = background.get_rect()

    FPS = 60
    FPS_CLOCK = pygame.time.Clock()
    BLACK = pygame.Color(0, 0, 0)

    SCREEN.fill(BLACK)

    theme.play(-1)

    i = 0
    j = 0
    change = 0

    all_sprites = pygame.sprite.Group()

    r1 = Roy()
    n1 = Natasha()
    a1 = Athos()
    s1 = Soldier()
    all_sprites.add(r1, n1, a1, s1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and change is 2:
                    change = 3
                    j = 0
                elif event.key == pygame.K_RETURN and change is 4:
                    change = 5
                    j = 0
                elif event.key == pygame.K_RETURN and change is 5:
                    change = 6
                    j = 0
                elif event.key == pygame.K_RETURN and change is 7:
                    change = 8
                    j = 0
                elif event.key == pygame.K_RETURN and change is 8:
                    change = 9
                    j = 0
                elif event.key == pygame.K_RETURN and change is 9:
                    change = 10
                    j = 0
                elif event.key == pygame.K_RETURN and change is 10:
                    change = 11
                    j = 0
                elif event.key == pygame.K_RETURN and change is 11:
                    change = 12
                    j = 0
                elif event.key == pygame.K_RETURN and change is 12:
                    change = 13
                elif event.key == pygame.K_RETURN and change is 18:
                    change = 19
                    j = 0
                elif event.key == pygame.K_RETURN and change is 20:
                    change = 21
                    j = 0
                elif event.key == pygame.K_RETURN and change is 21:
                    change = 22
                    j = 0
        background.set_alpha(i)
        SCREEN.fill(BLACK)

        if i != 255 and change is 0:
            SCREEN.blit(background, rect)
            i += 5
            pygame.time.delay(100)
        elif i is 255 and change is 0 or change is 1 or change is 2:
            SCREEN.blit(background, rect)
            change = 1
            FPS = 30
            if r1.x == 600:
                SCREEN.blit(background, rect)
                text_bubble.set_alpha(j)
                text_arrow.set_alpha(j)
                if j != 255:
                    SCREEN.blit(pygame.transform.scale(text_bubble, (800, 200)), (40, 70))
                    SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (700, 268))
                    j += 15
                    FPS = 30
                else:
                    SCREEN.blit(pygame.transform.scale(line_1, (800, 200)), (40, 70))
                    SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (700, 268))

                    change = 2
                    FPS = 15
        else:
            pass

        if change is 3:
            SCREEN.blit(background, rect)
            FPS = 30
            if n1.x == 320:
                SCREEN.blit(background, rect)
                text_bubble.set_alpha(j)
                text_arrow.set_alpha(j)
                if j != 255:
                    SCREEN.blit(pygame.transform.scale(text_bubble, (800, 200)), (40, 70))
                    SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (420, 268))
                    j += 15
                    FPS = 30
                else:
                    change = 4
                    FPS = 15
        if change is 4:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(line_2, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (420, 268))
            FPS = 15
        if change is 5:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(line_3, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (700, 268))
            FPS = 15
        if change is 6:
            SCREEN.blit(background, rect)
            FPS = 30
            if a1.x == 20:
                SCREEN.blit(background, rect)
                text_bubble.set_alpha(j)
                text_arrow.set_alpha(j)
                if j != 255:
                    SCREEN.blit(pygame.transform.scale(text_bubble, (800, 200)), (40, 70))
                    SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (140, 268))
                    j += 15
                    FPS = 30
                else:
                    change = 7
        if change is 7:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(line_4, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (140, 268))
            FPS = 15
        if change is 8:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(line_5, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (700, 268))
            FPS = 15
        if change is 9:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(line_6, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (140, 268))
            FPS = 15
        if change is 10:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(line_7, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (700, 268))
            FPS = 15
        if change is 11:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(line_8, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (140, 268))
            FPS = 15
        if change is 12:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(line_9, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (700, 268))
            FPS = 15
        if change is 13:
            SCREEN.blit(background, rect)
            if i is 0:
                change = 14
            else:
                i -= 5
        if change is 14:
            theme.stop()
            r1.x = 1000
            r1.alpha_val = 255
            n1.x = -250
            n1.alpha_val = 255
            a1.x = 1000
            a1.alpha_val = 255
            theme2.play(-1)
            change = 15
        if change is 15:
            desert_background.set_alpha(i)
            SCREEN.blit(desert_background, rect)
            if i != 255:
                i += 5
            else:
                change = 16
        if change is 16:
            FPS = 30
            SCREEN.blit(desert_background, rect)
            if r1.x == 400:
                change = 17
        if change is 17:
            SCREEN.blit(desert_background, rect)
            if a1.x == 600:
                SCREEN.blit(desert_background, rect)
                text_bubble.set_alpha(j)
                text_arrow.set_alpha(j)
                if j != 255:
                    SCREEN.blit(pygame.transform.scale(text_bubble, (800, 200)), (40, 70))
                    SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (700, 268))
                    j += 15
                    FPS = 30
                else:
                    change = 18
        if change is 18:
            FPS = 15
            SCREEN.blit(desert_background, rect)
            SCREEN.blit(pygame.transform.scale(line_9a, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (700, 268))
        if change is 19:
            FPS = 30
            SCREEN.blit(desert_background, rect)
            if s1.x == 100:
                SCREEN.blit(desert_background, rect)
                text_bubble.set_alpha(j)
                text_arrow.set_alpha(j)
                if j != 255:
                    SCREEN.blit(pygame.transform.scale(text_bubble, (800, 200)), (40, 70))
                    SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (220, 268))
                    j += 15
                    FPS = 30
                else:
                    change = 20
        if change is 20:
            FPS = 15
            SCREEN.blit(desert_background, rect)
            SCREEN.blit(pygame.transform.scale(line_10, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (220, 268))
        if change is 21:
            FPS = 15
            SCREEN.blit(desert_background, rect)
            SCREEN.blit(pygame.transform.scale(line_11, (800, 200)), (40, 70))
            SCREEN.blit(pygame.transform.scale(text_arrow, (50, 30)), (480, 268))
        if change is 22:
            desert_background.set_alpha(i)
            SCREEN.blit(desert_background, rect)
            if i is 0:
                pass
            else:
                i -= 5
                theme2.stop()
                main3()

        all_sprites.update(change, SCREEN)
        pygame.display.flip()
        FPS_CLOCK.tick(FPS)
if __name__ == "__main__":
    main2()
