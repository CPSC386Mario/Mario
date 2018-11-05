import sys
import pygame


def update_screen(screen, mario, settings, level, pipes, display, stats, lvl_map, bricks, upgrades):
    screen.fill(settings.bg_color)
    mario.update()
    upgrades.update()
    # level.blitme()
    mario.blitme()
    bricks.draw(screen)
    pipes.draw(screen)
    upgrades.draw(screen)
    display.score_blit(screen, stats)
    stats.update_time()

    if stats.game_over is True:
        screen.fill((0, 0, 0))
        display.over_blit(screen)

    pygame.display.flip()


def check_events(mario):
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
