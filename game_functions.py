import sys
import pygame


def update_screen(screen, mario, settings, level, pipes, display, stats, lvl_map, bricks, upgrades, enemies, flags,
                  poles, secret_bricks, secret_pipes):
    screen.fill(settings.bg_color)
    if stats.flag_reach_bot and stats.timer <= 100:
        mario.move_right()
        stats.timer += 1
    if stats.timer >= 100:
        mario.move_stop()
    flags.update()
    upgrades.update()
    enemies.update()
    # level.blitme()
    mario.update(stats, level)
    mario.blitme()
    mario.check_collision(screen, stats, display)

    # Draws only if not in the underground level
    if not stats.secret_level:
        enemies.draw(screen)
        pipes.draw(screen)
        poles.draw(screen)
        flags.draw(screen)
        bricks.draw(screen)

    # Draws only if in underground level
    if stats.secret_level:
        secret_bricks.draw(screen)
        secret_pipes.draw(screen)
    upgrades.draw(screen)
    display.score_blit(screen, stats)
    stats.update_time()
    stats.update_txt()

    if stats.game_over is True:
        screen.fill((0, 0, 0))
        display.over_blit(screen)

    pygame.display.flip()


def check_events(mario, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                # Stops player control when Mario has collided with the flag pole
                if not stats.reached_pole:
                    if mario.rect.left >= 20:
                        mario.move_left()
            elif event.key == pygame.K_RIGHT:
                # Stops player control when Mario has collided with the flag pole
                if not stats.reached_pole:
                    mario.move_right()
            elif event.key == pygame.K_DOWN:
                mario.crouch = True
            elif event.key == pygame.K_SPACE:
                # Stops player control when Mario has collided with the flag pole
                if not stats.reached_pole:
                    if mario.y_change == 0:
                        mario.move_jump()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mario.move_stop()
            elif event.key == pygame.K_RIGHT:
                mario.move_stop()
            elif event.key == pygame.K_SPACE:
                mario.jump = False
            elif event.key == pygame.K_DOWN:
                mario.crouch = False
