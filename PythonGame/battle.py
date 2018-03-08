import pygame
import sys
import time
from pygame.locals import *
from main_char import Roy
from athos_char import Athos
from soldier_char import Soldier

def main3():
    pygame.init()
    pygame.mixer.init()

    window_size = (960, 539)
    SCREEN = pygame.display.set_mode(window_size)
    background = pygame.image.load('desert.png').convert()
    background.set_colorkey((0, 0, 0), RLEACCEL)
    background2 = pygame.image.load('desert_select.png').convert()
    background2.set_colorkey((0, 0, 0), RLEACCEL)
    cursor = pygame.image.load('cursor.png').convert()
    cursor.set_colorkey((255, 255, 255), RLEACCEL)
    block = pygame.image.load('block.png').convert()
    block.set_colorkey((0, 0, 0), RLEACCEL)
    background3 = pygame.image.load('textbubble.png').convert()
    background3.set_colorkey((0, 0, 0), RLEACCEL)
    congradulations = pygame.image.load('cong2.png').convert()
    background3.set_colorkey((255, 255, 255), RLEACCEL)

    theme = pygame.mixer.Sound("battletheme1.ogg")
    theme2 = pygame.mixer.Sound("hit.ogg")
    move = pygame.mixer.Sound("move.ogg")
    select = pygame.mixer.Sound("select.ogg")
    end = pygame.mixer.Sound("end.ogg")

    rect = background.get_rect()
    rect2 = background2.get_rect()

    FPS = 30
    FPS_CLOCK = pygame.time.Clock()
    BLACK = pygame.Color(0, 0, 0)

    SCREEN.fill(BLACK)

    theme.play(-1)
    change = 29
    i = 0

    cursor_x = 3
    cursor_y = 4
    dumx = 0
    dumy = 0

    all_sprites = pygame.sprite.Group()

    r1 = Roy()
    a1 = Athos()
    s1 = Soldier()

    all_sprites.add(r1, a1, s1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and (change is 31 or change is 32 or change is 33) and cursor_x != 851:
                    select.play()
                    cursor_x += 106
                if event.key == pygame.K_LEFT and (change is 31 or change is 32 or change is 33) and cursor_x != 3:
                    select.play()
                    cursor_x -= 106
                    print(a1.o_x)
                    print(a1.o_y)
                    print(s1.o_x)
                    print(s1.o_y)

                if event.key == pygame.K_UP and (change is 31 or change is 32 or change is 33) and cursor_y != 4:
                    select.play()
                    cursor_y -= 106
                if event.key == pygame.K_DOWN and (change is 31 or change is 32 or change is 33) and cursor_y != 428:
                    select.play()
                    cursor_y += 106
                if event.key == pygame.K_RETURN and change is 31 and r1.o_x - 3 == cursor_x and r1.o_y == cursor_y:
                    select.play()
                    change = 32
                if event.key == pygame.K_RETURN and change is 31 and a1.o_x - 3 == cursor_x and a1.o_y == cursor_y:
                    select.play()
                    change = 33
                if event.key == pygame.K_RETURN and change is 32 and dumx + 103 == cursor_x and dumy == cursor_y:
                    select.play()
                    r1.change_x = dumx + 106
                    r1.change_y = dumy
                    change = 60
                if event.key == pygame.K_RETURN and change is 32 and dumx + 209 == cursor_x and dumy == cursor_y:
                    select.play()
                    r1.change_x = dumx + 212
                    r1.change_y = dumy
                    change = 60
                if event.key == pygame.K_RETURN and change is 32 and dumx - 103 == cursor_x and dumy == cursor_y:
                    select.play()
                    r1.change_x = dumx - 100
                    r1.change_y = dumy
                    change = 60
                if event.key == pygame.K_RETURN and change is 32 and dumx - 206 == cursor_x and dumy == cursor_y:
                    select.play()
                    r1.change_x = dumx - 203
                    r1.change_y = dumy
                    change = 60
                if event.key == pygame.K_RETURN and change is 32 and dumx - 3 == cursor_x and dumy + 106 == cursor_y:
                    select.play()
                    r1.change_x = dumx
                    r1.change_y = dumy + 106
                    change = 60
                if event.key == pygame.K_RETURN and change is 32 and dumx - 3 == cursor_x and dumy + 212 == cursor_y:
                    select.play()
                    r1.change_x = dumx
                    r1.change_y = dumy + 212
                    change = 60
                if event.key == pygame.K_RETURN and change is 32 and dumx - 3 == cursor_x and dumy - 106 == cursor_y:
                    select.play()
                    r1.change_x = dumx
                    r1.change_y = dumy - 106
                    change = 60
                if event.key == pygame.K_RETURN and change is 32 and dumx - 3 == cursor_x and dumy - 212 == cursor_y:
                    select.play()
                    r1.change_x = dumx
                    r1.change_y = dumy - 212
                    change = 60

                if event.key == pygame.K_RETURN and change is 33 and dumx + 103 == cursor_x and dumy == cursor_y:
                    select.play()
                    a1.change_x = dumx + 106
                    a1.change_y = dumy
                    change = 61
                if event.key == pygame.K_RETURN and change is 33 and dumx - 109 == cursor_x and dumy == cursor_y:
                    select.play()
                    a1.change_x = dumx - 100
                    a1.change_y = dumy
                    change = 61
                if event.key == pygame.K_RETURN and change is 33 and dumx - 3 == cursor_x and dumy + 106 == cursor_y:
                    select.play()
                    a1.change_x = dumx
                    a1.change_y = dumy + 106
                    change = 61
                if event.key == pygame.K_RETURN and change is 33 and dumx - 3 == cursor_x and dumy - 106 == cursor_y:
                    select.play()
                    a1.change_x = dumx
                    a1.change_y = dumy - 106
                    change = 61
        SCREEN.fill(BLACK)

        if change is 29:
            i += 15
            background.set_alpha(i)
            SCREEN.blit(background, rect)
            if i == 255:
                change = 30
        if change is 30:
            move.play(-1)
            SCREEN.blit(background, rect)
            if s1.o_x == 850:
                change = 31
                move.stop()
        if change is 31:
            SCREEN.blit(background, rect)
            SCREEN.blit(cursor, (cursor_x, cursor_y))
            FPS = 10
        if change is 32:
            SCREEN.blit(background2, rect)
            SCREEN.blit(cursor, (cursor_x, cursor_y))
            FPS = 10

            dumx = r1.o_x
            dumy = r1.o_y

            if dumx + 106 <= 851:
                SCREEN.blit(block, (dumx + 109, dumy + 2))
            if dumx + 212 <= 851:
                SCREEN.blit(block, (dumx + 215, dumy + 2))
            if dumy + 106 <= 428:
                SCREEN.blit(block, (dumx + 3, dumy + 111))
            if dumy + 212 <= 428:
                SCREEN.blit(block, (dumx + 3, dumy + 217))
            if dumx - 106 >= 3:
                SCREEN.blit(block, (dumx - 109, dumy + 2))
            if dumx - 212 >= 3:
                SCREEN.blit(block, (dumx - 215, dumy + 2))
            if dumy - 106 >= 4:
                SCREEN.blit(block, (dumx + 3, dumy - 111))
            if dumy - 212 >= 4:
                SCREEN.blit(block, (dumx + 3, dumy - 217))
        if change is 33:
            SCREEN.blit(background2, rect)
            SCREEN.blit(cursor, (cursor_x, cursor_y))
            FPS = 10

            dumx = a1.o_x
            dumy = a1.o_y

            if dumx + 106 <= 851:
                SCREEN.blit(block, (dumx + 109, dumy + 2))
            if dumy + 106 <= 428:
                SCREEN.blit(block, (dumx + 3, dumy + 111))
            if dumx - 106 >= 3:
                SCREEN.blit(block, (dumx - 109, dumy + 2))
            if dumy - 106 >= 4:
                SCREEN.blit(block, (dumx + 3, dumy - 111))
        if change is 60:
            SCREEN.blit(background, rect)
            FPS = 60
            if r1.o_x == r1.change_x and r1.o_y == r1.change_y:
                dumx = 0
                dumy = 0
                r1.change_x = 0
                r1.change_y = 0
                change = 31

        if change is 61:
            SCREEN.blit(background, rect)
            FPS = 400
            if a1.o_x == a1.change_x and a1.o_y == a1.change_y:
                dumx = 0
                dumy = 0
                a1.change_x = 0
                a1.change_y = 0
                if a1.o_x + 102 == s1.o_x and a1.o_y == s1.o_y:
                    change = 100
                    theme.stop()
                    theme2.play()
                    time.sleep(theme2.get_length())
                    theme2.play()
                    time.sleep(theme2.get_length())
                    end.play()
                else:
                    change = 31
        if change is 100:
            SCREEN.blit(background, rect)
            SCREEN.blit(pygame.transform.scale(background3, (800, 500)), (100, 100))
            SCREEN.blit(congradulations, (300, 100))




        all_sprites.update(change, SCREEN)
        pygame.display.flip()
        FPS_CLOCK.tick(FPS)

if __name__ == "__main__":
    main3()