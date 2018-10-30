import pygame
from stats import Stats
import game_functions as gf
from mario import Mario


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mario")

    stats = Stats()
    mario = Mario(screen)

    while True:
        if stats.game_active:
            gf.check_events(screen, mario)
            gf.update_screen(screen, mario)
            pygame.display.flip()

run_game()