import pygame


class Stats:

    def __init__(self):
        self.game_active = True
        self.game_over = False

        self.reached_pole = False
        self.flag_reach_bot = False

        self.activate_secret = False
        self.activate_main_lvl = True
        self.secret_level = False
        self.main_level = True
        self.return_main_level = False

        self.score = 0
        self.coins = 0
        self.time = 400
        self.lives = 3
        self.timer = 0

        self.tick = pygame.time.get_ticks()

    def update_time(self):
        seconds = (pygame.time.get_ticks() - self.tick)/1000
        if seconds > 1:
            self.tick = pygame.time.get_ticks()
            self.time -= 1
        if self.time is 0:
            self.game_over = True
        elif self.time < -2:
            self.game_over = False
            self.reset_stats()
            # TO DO: Reset mario to starting position

    def reset_stats(self):
        self.score = 0
        self.coins = 0
        self.time = 400
        self.lives = 3
        self.game_over = False