import pygame


class Stats:

    def __init__(self):
        self.game_active = True
        self.game_over = False
        self.score = 0
        self.coins = 0
        self.time = 400
        self.lives = 3

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