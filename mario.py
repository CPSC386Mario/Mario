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
        self.small_star_mario = []
        self.shroom_mario = []
        self.flower_mario = []
        self.star_mario = []
        self.image = pygame.Surface((16, 16))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (59, 0, 17, 16))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        # Movement Flags
        self.moving_left = False
        self.moving_right = False
        self.jump = False
        self.facing_right = True

        for i in range(0, 13):
            # base mario
            temp_img = pygame.Surface((17, 16))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (59, i * 20, 17, 16))
            temp = pygame.transform.scale(temp_img, (40, 40))
            self.small_mario.append(temp)
            # small star mario
            temp_img = pygame.Surface((17, 16))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (80, i * 20, 17, 16))
            temp = pygame.transform.scale(temp_img, (40, 40))
            self.small_star_mario.append(temp)
            temp_img = pygame.Surface((17, 16))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (100, i * 20, 17, 16))
            temp = pygame.transform.scale(temp_img, (40, 40))
            self.small_star_mario.append(temp)
            # shroom mario
            temp_img = pygame.Surface((17, 32))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (120, i * 40, 17, 32))
            temp = pygame.transform.scale(temp_img, (40, 60))
            self.shroom_mario.append(temp)
            # flower mario
            temp_img = pygame.Surface((17, 32))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (140, i * 40, 17, 32))
            temp = pygame.transform.scale(temp_img, (40, 60))
            self.flower_mario.append(temp)
            self.star_mario.append(temp)
            # star mario
            temp_img = pygame.Surface((17, 32))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (160, i * 40, 17, 32))
            temp = pygame.transform.scale(temp_img, (40, 60))
            self.star_mario.append(temp)

        self.image = self.small_mario[0]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = self.settings.base_level
        self.x_change = 0
        self.y_change = 0

        self.frame_counter = 0
        self.flash_frame = 0

        # if fired is true, shroomed must be true, but can have shroom true and fired false
        # set shroomed and star true for big star mario
        self.dead = False
        self.shroomed = False
        self.fired = False
        self.star_pow = False

    def update(self):
        if self.dead:
            self.die_animate()
        else:
            if not self.shroomed and not self.star_pow:
                self.update_small()
            elif self.star_pow and not self.shroomed:
                self.update_star()
            elif self.shroomed and not self.fired and not self.star_pow:
                self.update_shroomed()
            elif self.fired and not self.star_pow:
                self.update_flowered()
            elif self.shroomed and self.star_pow:
                self.update_big_star()

    def update_small(self):
        self.move()
        if self.rect.y == self.settings.base_level - self.rect.height:
            self.jump = False

        if not self.moving_right and not self.moving_left and not self.jump:
            if self.facing_right:
                self.image = self.small_mario[0]
            else:
                self.image = self.small_mario[6]
        if self.moving_right and not self.jump:
            self.right_animate()
        if self.facing_right and self.jump:
            self.image = self.small_mario[5]
        if self.moving_left and not self.jump:
            self.left_animate()
        if not self.facing_right and self.jump:
            self.image = self.small_mario[11]

    def update_shroomed(self):
        self.move()
        if self.rect.y == self.settings.base_level - self.rect.height:
            self.jump = False

        if not self.moving_right and not self.moving_left and not self.jump:
            if self.facing_right:
                self.image = self.shroom_mario[0]
            else:
                self.image = self.shroom_mario[6]
        if self.moving_right and not self.jump:
            self.big_right_animate()
        if self.facing_right and self.jump:
            self.image = self.shroom_mario[5]
        if self.moving_left and not self.jump:
            self.big_left_animate()
        if not self.facing_right and self.jump:
            self.image = self.shroom_mario[11]

    def update_flowered(self):
        self.move()
        if self.rect.y == self.settings.base_level - self.rect.height:
            self.jump = False

        if not self.moving_right and not self.moving_left and not self.jump:
            if self.facing_right:
                self.image = self.flower_mario[0]
            else:
                self.image = self.flower_mario[6]
        if self.moving_right and not self.jump:
            self.flower_right_animate()
        if self.facing_right and self.jump:
            self.image = self.flower_mario[5]
        if self.moving_left and not self.jump:
            self.flower_left_animate()
        if not self.facing_right and self.jump:
            self.image = self.flower_mario[11]

    def update_star(self):
        self.move()
        if self.rect.y == self.settings.base_level - self.rect.height:
            self.jump = False

        if not self.moving_right and not self.moving_left and not self.jump:
            self.star_flash()
        if self.moving_right and not self.jump:
            self.right_star_flash()
        if self.facing_right and self.jump:
            self.right_star_jump()
        if self.moving_left and not self.jump:
            self.left_star_flash()
        if not self.facing_right and self.jump:
            self.left_star_jump()

    def update_big_star(self):
        self.move()
        if self.rect.y == self.settings.base_level - self.rect.height:
            self.jump = False

        if not self.moving_right and not self.moving_left and not self.jump:
            self.big_star_flash()
        if self.moving_right and not self.jump:
            self.big_right_star_flash()
        if self.facing_right and self.jump:
            self.big_right_star_jump()
        if self.moving_left and not self.jump:
            self.big_left_star_flash()
        if not self.facing_right and self.jump:
            self.big_left_star_jump()

    def star_flash(self):
        if self.frame_counter <= 50:
            if self.facing_right:
                self.image = self.small_star_mario[0]
            else:
                self.image = self.small_star_mario[12]
        elif self.frame_counter <= 100:
            if self.facing_right:
                self.image = self.small_star_mario[1]
            else:
                self.image = self.small_star_mario[13]
        elif self.frame_counter <= 150:
            if self.facing_right:
                self.image = self.small_mario[0]
            else:
                self.image = self.small_mario[6]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def right_star_jump(self):
        if self.frame_counter <= 50:
            self.image = self.small_star_mario[10]
        elif self.frame_counter <= 100:
            self.image = self.small_star_mario[11]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[5]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def right_star_flash(self):
        if self.frame_counter <= 50:
            self.image = self.small_star_mario[2]
        elif self.frame_counter <= 100:
            self.image = self.small_star_mario[5]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[3]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def right_animate(self):
        if self.frame_counter <= 50:
            self.image = self.small_mario[1]
        elif self.frame_counter <= 100:
            self.image = self.small_mario[2]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[3]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def left_star_jump(self):
        if self.frame_counter <= 50:
            self.image = self.small_star_mario[22]
        elif self.frame_counter <= 100:
            self.image = self.small_star_mario[23]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[11]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def left_star_flash(self):
        if self.frame_counter <= 50:
            self.image = self.small_star_mario[14]
        elif self.frame_counter <= 100:
            self.image = self.small_star_mario[17]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[9]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def left_animate(self):
        if self.frame_counter <= 50:
            self.image = self.small_mario[7]
        elif self.frame_counter <= 100:
            self.image = self.small_mario[8]
        elif self.frame_counter <= 150:
            self.image = self.small_mario[9]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_star_flash(self):
        if self.frame_counter <= 50:
            if self.facing_right:
                self.image = self.star_mario[0]
            else:
                self.image = self.star_mario[12]
        elif self.frame_counter <= 100:
            if self.facing_right:
                self.image = self.star_mario[1]
            else:
                self.image = self.star_mario[13]
        elif self.frame_counter <= 150:
            if self.facing_right:
                self.image = self.shroom_mario[0]
            else:
                self.image = self.shroom_mario[6]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_right_star_jump(self):
        if self.frame_counter <= 50:
            self.image = self.star_mario[10]
        elif self.frame_counter <= 100:
            self.image = self.star_mario[11]
        elif self.frame_counter <= 150:
            self.image = self.shroom_mario[5]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_right_star_flash(self):
        if self.frame_counter <= 50:
            self.image = self.star_mario[2]
        elif self.frame_counter <= 100:
            self.image = self.star_mario[5]
        elif self.frame_counter <= 150:
            self.image = self.shroom_mario[3]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_right_animate(self):
        if self.frame_counter <= 50:
            self.image = self.shroom_mario[1]
        elif self.frame_counter <= 100:
            self.image = self.shroom_mario[2]
        elif self.frame_counter <= 150:
            self.image = self.shroom_mario[3]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_left_star_jump(self):
        if self.frame_counter <= 50:
            self.image = self.star_mario[22]
        elif self.frame_counter <= 100:
            self.image = self.star_mario[23]
        elif self.frame_counter <= 150:
            self.image = self.shroom_mario[11]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_left_star_flash(self):
        if self.frame_counter <= 50:
            self.image = self.star_mario[14]
        elif self.frame_counter <= 100:
            self.image = self.star_mario[17]
        elif self.frame_counter <= 150:
            self.image = self.shroom_mario[9]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def big_left_animate(self):
        if self.frame_counter <= 50:
            self.image = self.shroom_mario[7]
        elif self.frame_counter <= 100:
            self.image = self.shroom_mario[8]
        elif self.frame_counter <= 150:
            self.image = self.shroom_mario[9]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def flower_right_animate(self):
        if self.frame_counter <= 50:
            self.image = self.flower_mario[1]
        elif self.frame_counter <= 100:
            self.image = self.flower_mario[2]
        elif self.frame_counter <= 150:
            self.image = self.flower_mario[3]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def flower_left_animate(self):
        if self.frame_counter <= 50:
            self.image = self.flower_mario[7]
        elif self.frame_counter <= 100:
            self.image = self.flower_mario[8]
        elif self.frame_counter <= 150:
            self.image = self.flower_mario[9]
        else:
            self.frame_counter = 0
        self.frame_counter += 4

    def move(self):
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
            self.jump = False

        block_collide = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_collide:
            if self.y_change > 0:
                self.rect.bottom = block.rect.top
            elif self.y_change < 0:
                self.rect.top = block.rect.bottom
            self.y_change = 0
            self.jump = False

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
        self.moving_left = True
        self.facing_right = False

    def move_right(self):
        self.x_change = 1
        self.moving_right = True
        self.facing_right = True

    def move_stop(self):
        self.x_change = 0
        self.moving_left = False
        self.moving_right = False

    def move_jump(self):
        self.y_change = -5
        self.jump = True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def die_animate(self):
        if self.frame_counter == 0:
            self.image = self.small_mario[12]
        elif self.frame_counter <= 100:
            self.rect.y -= 2
        elif self.frame_counter <= 200:
            self.rect.y += 2
        self.frame_counter += 1
