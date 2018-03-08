import pygame
import sys
import time
from pygame.locals import *
from assassin_char import Assassin
from cutscene1 import main2


def main():
    pygame.init()
    pygame.mixer.init()
    window_size = (960, 539)
    SCREEN = pygame.display.set_mode(window_size)
    menu_theme = pygame.mixer.Sound("main.ogg")
    cursor_sound = pygame.mixer.Sound("Cursor.ogg")
    weed = pygame.mixer.Sound("weed.ogg")
    select = pygame.mixer.Sound("select.ogg")
    image = pygame.image.load('logo2.png').convert()
    image.set_colorkey((0, 0, 0), RLEACCEL)
    image2 = pygame.image.load('background.png').convert()
    image2.set_colorkey((0, 0, 0), RLEACCEL)
    start = pygame.image.load('start.png')
    image4 = pygame.image.load('assassin.png')

    rect = image.get_rect()
    rect2 = image2.get_rect()
    rect3 = start.get_rect()

    i = 1
    x = 0
    j = 130
    k = 0

    start_i = 300
    start_j = 340



    FPS = 60
    FPS_CLOCK = pygame.time.Clock()

    # COLOR LIST
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)

    menu_theme.play(-1)

    # set the title of the window
    pygame.display.set_caption("Fire Emblem Clone")

    # change the initial background color to white
    SCREEN.fill(BLACK)

    all_sprites = pygame.sprite.Group()

    all_sprites.add(Assassin())

    while True:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()

        SCREEN.fill(BLACK)

        image.set_alpha(i)

        if i == 255:
            if j == 70:
                SCREEN.blit(image2, rect2)
                SCREEN.blit(image, (240, j))
                if start_i != 350 and start_j == 340:
                    SCREEN.blit(start, (start_i, start_j))
                    start_i += 1
                if start_i == 350 and start_j != 290:
                    SCREEN.blit(start, (start_i, start_j))
                    start_j -= 1

                if start_i != 300 and start_j == 290:
                    SCREEN.blit(start, (start_i, start_j))
                    start_i -= 1
                if start_i == 300 and start_j != 340:
                    SCREEN.blit(start, (start_i, start_j))
                    start_j += 1


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        select.play()
                        k = 1
                        i = 254

            else:
                j -= 1
                SCREEN.blit(image2, rect2)
                SCREEN.blit(image, (240, j))
                #pygame.time.delay(20)

        elif k is 1:
            image.set_alpha(i)
            image2.set_alpha(i)
            SCREEN.blit(image2, rect2)
            i -= 5

            if i <= 0:
                i = 0
                if i is 0 and x is 0:
                    menu_theme.stop()
                    weed.play()
                    time.sleep(weed.get_length())
                    main2()
                    break
        else:
            SCREEN.blit(image2, rect2)
            SCREEN.blit(image, (240, j))
            #pygame.time.delay(20)
            i += 1
        #all_sprites.update(SCREEN)
        pygame.display.flip() # Update the display when all events have been processed
        FPS_CLOCK.tick(FPS)

if __name__ == "__main__":
    main()
