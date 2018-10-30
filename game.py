import pygame
from stats import Stats
import game_functions as gf
from mario import Mario
from settings import Settings

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    stats = Stats()
    mario = Mario(screen, settings)

    while True:
        if stats.game_active:
            gf.check_events(screen, mario)
            gf.update_screen(screen, mario, settings)
            pygame.display.flip()


run_game()
