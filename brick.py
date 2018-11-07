import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
    BRICK_SIZE = 40

    def __init__(self, screen, settings, block_type):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.block_type = block_type
        self.change_brick = False

        self.sz = Brick.BRICK_SIZE
        self.brick = "images/Red_Brick.png"
        self.item_brick = "images/Item_Brick.png"
        self.stone = "images/Ground_Brick.png"
        self.stair_brick = "images/Stair_Brick.png"
        self.empty_brick = "images/Empty_Brick.png"
        self.invisible_brick = "images/Invisible_Block.png"
        self.blue_brick = "images/Blue_Brick.png"
        self.blue_stone = "images/Blue_Stone.png"

        # Checks what type of brick needs to be drawn
        if block_type == 0:
            self.image = pygame.image.load(self.brick)
        if block_type == 1:
            self.image = pygame.image.load(self.item_brick)
        if block_type == 2:
            self.image = pygame.image.load(self.item_brick)
        if block_type == 3:
            self.image = pygame.image.load(self.stone)
        if block_type == 4:
            self.image = pygame.image.load(self.stair_brick)
        if block_type == 5:
            self.image = pygame.image.load(self.brick)
        if block_type == 6:
            self.image = pygame.image.load(self.invisible_brick)
        if block_type == 7:
            self.image = pygame.image.load(self.blue_brick)
        if block_type == 8:
            self.image = pygame.image.load(self.blue_stone)
        if block_type == 9:
            self.image = pygame.image.load(self.brick)

        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def change(self):
        """Changes brick to empty brick"""
        self.image = pygame.image.load(self.empty_brick)
        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))
