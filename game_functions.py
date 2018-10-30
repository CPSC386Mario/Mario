import sys
import pygame


def update_screen(screen, mario):
    screen.fill((0, 255, 255))
    mario.blitme()
    pygame.display.flip()


def check_events(screen, mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
