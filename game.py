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
from flag import Flag
from pole import Pole


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    # Groups for sprites
    pipes = Group()
    secret_pipes = Group()
    bricks = Group()
    secret_bricks = Group()
    upgrades = Group()
    enemies = Group()
    poles = Group()
    flags = Group()

    stats = Stats()
    # Stores pipes for secret level in secret_pipes group
    for i in range(6, 8):
        pipe = Pipe(screen, settings, i)
        secret_pipes.add(pipe)

    # Create and initialize flag and pole before storing in group
    flag = Flag(screen, settings, stats)
    flags.add(flag)
    pole = Pole(screen, settings)
    poles.add(pole)

    lvl_map = None
    level = Level(screen, settings, pipes, bricks, upgrades, enemies, flags, poles)
    display = Display(screen, stats)
    mario = Mario(screen, settings, pipes, bricks, upgrades, stats, enemies, poles, secret_bricks, secret_pipes, level)


    while True:
        # Checks if Mario is in the main level and sets the map, generate the bricks, pipes, flags, and pole
        # Does this only once
        if stats.activate_main_lvl:
            lvl_map = Map(screen, settings, bricks, pipes, mario, enemies, upgrades, stats, secret_bricks)
            lvl_map.build_brick()
            # generate pipes and flag/pole
            for i in range(0, 6):
                pipe = Pipe(screen, settings, i)
                pipes.add(pipe)
            flag = Flag(screen, settings, stats)
            flags.add(flag)
            pole = Pole(screen, settings)
            poles.add(pole)
            stats.activate_main_lvl = False

        # Checks if Mario has activated the secret level and sets the map, clears all of the main level
        # Does this only once
        if stats.activate_secret:
            # Clears everything belonging to main level to prevent lag
            pipes.empty()
            bricks.empty()
            enemies.empty()
            poles.empty()
            flags.empty()
            lvl_map = Map(screen, settings, bricks, pipes, mario, enemies, upgrades, stats, secret_bricks)
            lvl_map.build_brick()

            stats.activate_secret = False
            stats.main_level = False

        if stats.game_active:
            gf.check_events(mario, stats)

            # If the player gets near the right side, shift the world left (-x)
            if mario.rect.right >= 600 and stats.main_level:
                diff = mario.rect.right - 600
                mario.rect.right = 600
                level.shifting_world(-diff)

            gf.update_screen(screen, mario, settings, level, pipes, display, stats, lvl_map, bricks, upgrades, enemies,
                             flags, poles, secret_bricks, secret_pipes)
            pygame.display.flip()


run_game()
