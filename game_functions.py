import sys
import pygame


def update_screen(screen, mario, settings, level, pipes):
    screen.fill(settings.bg_color)
    mario.update()
    level.blitme()
    mario.blitme()
    pipes.draw(screen)
    pygame.display.flip()


def check_events(screen, mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                mario.moving_left = True
            elif event.key == pygame.K_RIGHT:
                mario.moving_right = True
            elif event.key == pygame.K_SPACE:
                mario.jump = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mario.moving_left = False
            elif event.key == pygame.K_RIGHT:
                mario.moving_right = False
            elif event.key == pygame.K_SPACE:
                mario.jump = False
