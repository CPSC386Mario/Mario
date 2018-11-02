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
                mario.move_left()
            elif event.key == pygame.K_RIGHT:
                mario.move_right()
            elif event.key == pygame.K_SPACE:
                mario.move_jump()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mario.move_stop()
            elif event.key == pygame.K_RIGHT:
                mario.move_stop()
            elif event.key == pygame.K_SPACE:
                mario.jump = False
