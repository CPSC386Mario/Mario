import pygame


class Level:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/level_bg.png')
        self.image = pygame.transform.scale(self.image, (7500, self.settings.screen_height))
        self.rect = self.image.get_rect()

        self.shift_world = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def shifting_world(self, shifting_x):
        self.shift_world += shifting_x

        self.rect.x += shifting_x
