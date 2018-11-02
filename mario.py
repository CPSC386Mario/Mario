import pygame
from pygame.sprite import Sprite


class Mario(Sprite):

    def __init__(self, screen, settings, pipes, blocks):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.blocks = blocks
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
            temp_img = pygame.Surface((11, 16))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (60, i * 20, 16, 16))
            temp = pygame.transform.scale(temp_img, (30, 40))
            self.small_mario.append(temp)

        self.image = self.small_mario[0]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = self.settings.base_level
        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.calc_gravity()

        self.rect.x += self.x_change

        pipe_collide = pygame.sprite.spritecollide(self, self.pipes, False)
        for pipe in pipe_collide:
            if self.x_change > 0:
                self.rect.right = pipe.rect.left
            if self.x_change < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = pipe.rect.right

        block_collide = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_collide:
            if self.x_change > 0:
                self.rect.right = block.rect.left
            if self.x_change < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        self.rect.y += self.y_change

        pipe_collide = pygame.sprite.spritecollide(self, self.pipes, False)
        for pipe in pipe_collide:
            if self.y_change > 0:
                self.rect.bottom = pipe.rect.top
            elif self.y_change < 0:
                self.rect.top = pipe.rect.bottom
            self.y_change = 0

        block_collide = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_collide:
            if self.y_change > 0:
                self.rect.bottom = block.rect.top
            elif self.y_change < 0:
                self.rect.top = block.rect.bottom
            self.y_change = 0

    def calc_gravity(self):
        if self.y_change == 0:
            self.y_change = 1
        else:
            self.y_change += .05
        if self.rect.y >= self.settings.base_level - self.rect.height and self.y_change >= 0:
            self.y_change = 0
            self.rect.y = self.settings.base_level - self.rect.height

    def move_left(self):
        self.x_change = -1

    def move_right(self):
        self.x_change = 1

    def move_stop(self):
        self.x_change = 0

    def move_jump(self):
        self.y_change = -5

    def blitme(self):
        self.screen.blit(self.image, self.rect)
