import pygame
from pygame.sprite import Sprite


class Koopa(Sprite):

    def __init__(self, screen, settings, pipes, blocks, enemies, mario):
        super(Koopa, self).__init__()
        self.screen = screen
        self.settings = settings
        self.pipes = pipes
        self.blocks = blocks
        self.screen_rect = screen.get_rect()
        self.enemies = enemies
        self.mario = mario

        self.frames = []
        self.image = pygame.Surface((15, 15))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (19, 0, 16, 23))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        self.moving_left = False
        self.kicked = False

        for i in range(0, 5):
            temp_img = pygame.Surface((16, 23))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (19, i*30, 16, 23))
            temp = pygame.transform.scale(temp_img, (40, 60))
            self.frames.append(temp)

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.x_change = 0.5
        self.y_change = 0.0

        self.frame_counter = 0
        self.stunned = False

        # allows for Mario to check the difference between Goomba and Koopa
        self.enemy_type = 1

    def update(self):
        if self.stunned:
            self.image = self.frames[4]
            if self.kicked:
                self.move()
                # Kills all enemies it comes into contact with in shell form
                pygame.sprite.spritecollide(self, self.enemies, True)
                if pygame.sprite.spritecollide(self, self.mario, False):
                    self.mario.dead = True

        else:
            self.move()
            if self.frame_counter <= 100:
                if self.moving_left:
                    self.image = self.frames[0]
                else:
                    self.image = self.frames[3]
                self.frame_counter += 1
            elif self.frame_counter <= 200:
                if self.moving_left:
                    self.image = self.frames[1]
                else:
                    self.image = self.frames[2]
                self.frame_counter += 1
            else:
                self.frame_counter = 0

    def move(self):
        self.calc_gravity()

        pipe_collide = pygame.sprite.spritecollide(self, self.pipes, False)
        for pipe in pipe_collide:
            if self.x_change > 0:
                self.rect.right = pipe.rect.left
            if self.x_change < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = pipe.rect.right
            self.x_change *= -1
            self.swap_bool()

        block_collide = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_collide:
            if self.x_change > 0:
                self.rect.right = block.rect.left
            if self.x_change < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            self.x_change *= -1
            self.swap_bool()

        block_collide = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_collide:
            if self.y_change > 0:
                self.rect.bottom = block.rect.top
            self.y_change = 0

        self.rect.x += self.x_change
        self.rect.y += self.y_change

    def calc_gravity(self):
        if self.y_change == 0:
            self.y_change = 1
        else:
            self.y_change += .05
        if self.rect.y >= self.settings.base_level - self.rect.height and self.y_change >= 0:
            self.y_change = 0
            self.rect.y = self.settings.base_level - self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def swap_bool(self):
        if self.moving_left:
            self.moving_left = False
        else:
            self.moving_left = True
