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
        self.bottom_brick = "images/Ground_Brick.png"
        self.stair_brick = "images/Stair_Brick.png"
        self.empty_brick = "images/Empty_Brick.png"
        self.invisible_brick = "images/Invisible_Block.png"

        # Checks what type of brick needs to be drawn
        if block_type == 0:
            self.image = pygame.image.load(self.brick)
        if block_type == 1:
            self.image = pygame.image.load(self.item_brick)
        if block_type == 2:
            self.image = pygame.image.load(self.item_brick)
        if block_type == 3:
            self.image = pygame.image.load(self.bottom_brick)
        if block_type == 4:
            self.image = pygame.image.load(self.stair_brick)
        if block_type == 5:
            self.image = pygame.image.load(self.brick)
        if block_type == 6:
            self.image = pygame.image.load(self.invisible_brick)

        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.og_pos = self.rect.y
        self.frame_counter = 0
        self.bouncing = False

    def change(self):
        self.image = pygame.image.load(self.empty_brick)
        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))

    def update(self):
        if self.bouncing:
            if self.frame_counter <= 5:
                self.rect.y -= 1
            elif self.frame_counter <= 10:
                self.rect.y += 1
            else:
                self.frame_counter = 0
                self.bouncing = False
            self.frame_counter += 1
