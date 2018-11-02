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
        self.pipe_loc = [1000, 1400, 100, 2000, 5100, 5500]
        self.height = [100, 146, 200]
        self.image = pygame.Surface((40, 100))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (200, 0, 40, 40))
        self.image = pygame.transform.scale(self.image, (120, 100))
        self.rect = self.image.get_rect()

        temp_img1 = pygame.Surface((32, 33))
        temp_img1.set_colorkey((0, 0, 0))
        temp_img1.blit(sheet, (0, 0), (200, 0, 40, 40))
        temp1 = pygame.transform.scale(temp_img1, (90, 100))
        self.pipe.append(temp1)

        temp_img2 = pygame.Surface((32, 100))
        temp_img2.set_colorkey((0, 0, 0))
        temp_img2.blit(sheet, (0, 0), (200, 40, 40, 50))
        temp2 = pygame.transform.scale(temp_img2, (90, 300))
        self.pipe.append(temp2)

        temp_img3 = pygame.Surface((32, 100))
        temp_img3.set_colorkey((0, 0, 0))
        temp_img3.blit(sheet, (0, 0), (200, 70, 40, 40))
        temp3 = pygame.transform.scale(temp_img3, (90, 500))
        self.pipe.append(temp3)

        self.image = self.pipe[self.num]
        self.rect = self.image.get_rect()
        self.rect.x = self.pipe_loc[self.num]
        self.rect.y = self.settings.base_level - self.height[self.num]

    def blitme(self):
        self.screen.blit(self.image, self.rect)
