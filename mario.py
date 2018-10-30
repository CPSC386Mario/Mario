import pygame
from pygame.sprite import Sprite


class Mario(Sprite):

    def __init__(self, screen):
        super(Mario, self).__init__()
        self.screen = screen
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

        for i in range(0, 13):
            temp_img = pygame.Surface((16, 16))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (60, i * 20, 16, 16))
            temp = pygame.transform.scale(temp_img, (50, 50))
            self.small_mario.append(temp)

        self.image = self.small_mario[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery + 100

    def update(self):
        if self.moving_right:
            self.rect.x += 5
        elif self.moving_left:
            self.rect.x -= 5

    def blitme(self):
        self.screen.blit(self.image, self.rect)
