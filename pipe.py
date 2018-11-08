import pygame
from pygame.sprite import Sprite


class Pipe(Sprite):
    def __init__(self, screen, settings, num):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.num = num
        self.screen_rect = screen.get_rect()

        self.pipe = []
        self.pipe_loc = [1150, 1450, 1800, 2260, 6600, 7200]
        self.height = [83, 125, 167, 167, 83, 83]
        self.image = pygame.Surface((40, 200))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (200, 0, 40, 40))
        self.image = pygame.transform.scale(self.image, (120, 100))
        self.rect = self.image.get_rect()

        temp_img1 = pygame.Surface((32, 33))
        temp_img1.set_colorkey((0, 0, 0))
        temp_img1.blit(sheet, (0, 0), (200, 0, 40, 40))
        temp1 = pygame.transform.scale(temp_img1, (80, 85))

        temp_img2 = pygame.Surface((32, 100))
        temp_img2.set_colorkey((0, 0, 0))
        temp_img2.blit(sheet, (0, 0), (200, 40, 40, 50))
        temp2 = pygame.transform.scale(temp_img2, (80, 260))

        temp_img3 = pygame.Surface((32, 200))
        temp_img3.set_colorkey((0, 0, 0))
        temp_img3.blit(sheet, (0, 0), (200, 90, 40, 80))
        temp3 = pygame.transform.scale(temp_img3, (80, 520))

        self.pipe.append(temp1)
        self.pipe.append(temp2)
        self.pipe.append(temp3)
        self.pipe.append(temp3)
        self.pipe.append(temp1)
        self.pipe.append(temp1)

        self.image = self.pipe[self.num]
        self.rect = self.image.get_rect()
        self.rect.x = self.pipe_loc[self.num]
        self.rect.y = self.settings.base_level - self.height[self.num]

    def blitme(self):
        self.screen.blit(self.image, self.rect)
