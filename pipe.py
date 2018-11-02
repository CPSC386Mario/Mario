import pygame
from pygame.sprite import Sprite


class Pipe(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.small_pipe = []
        self.image = pygame.Surface((40, 40))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (200, 0, 40, 40))
        self.image = pygame.transform.scale(self.image, (120, 100))
        self.rect = self.image.get_rect()

        for i in range(0, 13):
            temp_img = pygame.Surface((32, 33))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (200, i * 20, 40, 40))
            temp = pygame.transform.scale(temp_img, (90, 100))
            self.small_pipe.append(temp)

        self.image = self.small_pipe[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.settings.base_level-98

    def blitme(self):
        self.screen.blit(self.image, self.rect)
