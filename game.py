import pygame
from pygame.sprite import Group
from stats import Stats
import game_functions as gf
from mario import Mario
from settings import Settings
from level import Level
from pipe import Pipe
from display import Display
from map import Map


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    pipes = Group()
    bricks = Group()

    stats = Stats()
    for i in range(0, 6):
        pipe = Pipe(screen, settings, i)
        pipes.add(pipe)
    lvl_map = Map(screen, settings, bricks, mapfile='images/level_loc.txt')
    mario = Mario(screen, settings, pipes)
    level = Level(screen, settings, pipes, lvl_map, bricks)
    display = Display(screen, stats)

    lvl_map.build_brick()
    while True:
        if stats.game_active:
            gf.check_events(mario)

            # If the player gets near the right side, shift the world left (-x)
            if mario.rect.right >= 600:
                diff = mario.rect.right - 600
                mario.rect.right = 600
                level.shifting_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if mario.rect.left <= 120:
                diff = 120 - mario.rect.left
                mario.rect.left = 120
                level.shifting_world(diff)

            gf.update_screen(screen, mario, settings, level, pipes, display, stats, lvl_map, bricks)
            pygame.display.flip()


run_game()
