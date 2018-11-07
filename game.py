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
    radio = pygame.mixer
    radio.init()
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    clips = [radio.Sound('sounds/bg_music.wav'), radio.Sound('sounds/block_bump.wav'),
             radio.Sound('sounds/brick_break.wav'), radio.Sound('sounds/coin.wav'),
             radio.Sound('sounds/death.wav'), radio.Sound('sounds/extra_life.wav'),
             radio.Sound('sounds/fireball.wav'), radio.Sound('sounds/jump.wav'), radio.Sound('sounds/kill.wav'),
             radio.Sound('sounds/pipe.wav'), radio.Sound('sounds/power_spawn.wav'),
             radio.Sound('sounds/powerup.wav'), radio.Sound('sounds/stage_clear.wav'), radio.Sound('sounds/star.wav')]

    pipes = Group()
    bricks = Group()
    upgrades = Group()
    enemies = Group()
    poles = Group()
    fireballs = Group()
    ground = Group()  # +

    stats = Stats()
    for i in range(0, 6):
        pipe = Pipe(screen, settings, i)
        pipes.add(pipe)
    flag = Flag(screen, settings, stats)
    pole = Pole(screen, settings)
    poles.add(pole)
    mario = Mario(screen, settings, pipes, bricks, upgrades, stats, enemies, poles, radio, clips, fireballs)
    lvl_map = Map(screen, settings, bricks, pipes, mario, enemies, ground, mapfile='images/level_loc.txt')  # +
    level = Level(screen, settings, pipes, lvl_map, bricks, upgrades, enemies, flag, poles)
    display = Display(screen, stats)

    lvl_map.build_brick()
    clips[0].play(-1)
    while True:
        if stats.game_active:
            gf.check_events(mario, stats, clips, fireballs)

            # If the player gets near the right side, shift the world left (-x)
            if mario.rect.right >= 600:
                diff = mario.rect.right - 600
                mario.rect.right = 600
                level.shifting_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            # if mario.rect.left <= 100:
            #    diff = 100 - mario.rect.left
            #    mario.rect.left = 100
            #    level.shifting_world(diff)

            gf.update_screen(screen, mario, settings, level, pipes, display, stats, bricks, upgrades, enemies,
                             flag, poles, radio, clips, fireballs)
            pygame.display.flip()


run_game()
