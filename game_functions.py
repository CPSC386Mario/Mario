import sys
import pygame


def update_screen(screen, mario, settings, level, pipes, display, stats, bricks, upgrades, enemies, flag,
                  poles, radio, clips, fireballs):
    screen.fill(settings.bg_color)
    level.blitme()
    if stats.flag_reach_bot and stats.timer <= 100:
        mario.move_right()
        stats.timer += 1
    if stats.timer >= 100:
        mario.move_stop()
    mario.update()
    fireballs.update()
    check_fire_enemy_collisions(enemies, fireballs)
    flag.update()
    upgrades.update()
    for enemy in enemies:
        enemy.update(mario)
    bricks.update()
    # level.blitme()
    mario.blitme()
    fireballs.draw(screen)
    enemies.draw(screen)
    bricks.draw(screen)
    pipes.draw(screen)
    poles.draw(screen)
    flag.blitme()
    upgrades.draw(screen)
    display.score_blit(screen, stats)
    stats.update_time(radio, clips)

    if stats.game_over is True:
        screen.fill((0, 0, 0))
        display.over_blit(screen)

    pygame.display.flip()


def check_events(mario, stats, clips, fireballs):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                if not stats.reached_pole:
                    if mario.rect.left >= 20:
                        mario.move_left()
            elif event.key == pygame.K_RIGHT:
                if not stats.reached_pole:
                    mario.move_right()
            elif event.key == pygame.K_SPACE:
                if not stats.reached_pole:
                    if mario.y_change == 0:
                        clips[7].play()
                        mario.move_jump()
            elif event.key == pygame.K_x:
                if not stats.reached_pole and mario.fired and len(fireballs) <= 1:
                    mario.fire()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mario.move_stop()
            elif event.key == pygame.K_RIGHT:
                mario.move_stop()
            # elif event.key == pygame.K_SPACE:
            #     mario.jump = False   REMOVE THIS IN MAIN BUILD


def check_fire_enemy_collisions(enemies, fireballs):
    pygame.sprite.groupcollide(enemies, fireballs, True, True)
    # add score for fireball kill here
