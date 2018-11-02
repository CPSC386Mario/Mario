import pygame
from maze import Maze


class Level:
    def __init__(self, screen, settings, pipes, blocks):
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.blocks = blocks
        self.image = pygame.image.load('images/level_bg_temp.png')
        self.image = pygame.transform.scale(self.image, (8000, self.settings.screen_height))
        self.rect = self.image.get_rect()

        self.shift_world = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def shifting_world(self, shifting_x):
        self.shift_world += shifting_x

        self.rect.x += shifting_x

        for pipe in self.pipes:
            pipe.rect.x += shifting_x
        for block in self.blocks:
            block.rect.x += shifting_x

