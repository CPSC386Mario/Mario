import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
    BRICK_SIZE = 40

    def __init__(self, screen, settings, type):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.type = type

        self.sz = Brick.BRICK_SIZE
        self.brick = "images/Red_Brick.png"
        self.item_brick = "images/Item_Brick.png"
        self.bottom_brick = "images/point.bmp"
        if type == 0:
            self.image = pygame.image.load(self.brick)
        if type == 1:
            self.image = pygame.image.load(self.item_brick)
        if type == 2:
            self.image = pygame.image.load(self.bottom_brick)
        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

