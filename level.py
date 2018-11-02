import pygame


class Level:
    def __init__(self, screen, settings, pipes, lvl_map, bricks):
        self.screen = screen
        self.settings = settings
        self.bricks = bricks
        self.lvl_map = lvl_map
        self.pipes = pipes
        self.image = pygame.image.load('images/level_bg_ref.png')
        self.image = pygame.transform.scale(self.image, (8500, self.settings.screen_height))
        self.rect = self.image.get_rect()

        self.shift_world = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def shifting_world(self, shifting_x):
        self.shift_world += shifting_x

        self.rect.x += shifting_x

        for brick in self.bricks:
            brick.rect.x += shifting_x
        for pipe in self.pipes:
            pipe.rect.x += shifting_x
