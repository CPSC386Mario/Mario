import pygame
from pygame.sprite import Sprite


class Mario(Sprite):

    def __init__(self, screen, settings):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.small_mario = []
        self.image = pygame.Surface((16, 16))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (60, 0, 16, 16))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Movement Flags
        self.moving_left = False
        self.moving_right = False
        self.jump = False

        for i in range(0, 13):
            temp_img = pygame.Surface((16, 16))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (60, i * 20, 16, 16))
            temp = pygame.transform.scale(temp_img, (50, 50))
            self.small_mario.append(temp)

        self.image = self.small_mario[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.settings.screen_height
        self.y_change = 0

    def update(self):
        self.calc_gravity()

        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.jump:
            if self.rect.bottom >= self.settings.screen_height:
                self.y_change = -5
        self.rect.y += self.y_change

    def calc_gravity(self):
        if self.y_change == 0:
            self.y_change = 1
        else:
            self.y_change += .05
        if self.rect.y >= self.settings.screen_height - self.rect.height and self.y_change >= 0:
            self.y_change = 0
            self.rect.y = self.settings.screen_height - self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)
