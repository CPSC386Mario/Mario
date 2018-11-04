import pygame
from pygame.sprite import Sprite
from upgrade import Upgrade


class Mario(Sprite):

    def __init__(self, screen, settings, pipes, bricks, upgrades, stats):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.pipes = pipes
        self.bricks = bricks
        self.upgrades = upgrades
        self.screen_rect = screen.get_rect()

        self.small_mario = []
        self.image = pygame.Surface((16, 16))
        sheet = pygame.image.load('images/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (60, 0, 16, 16))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        for i in range(0, 13):
            temp_img = pygame.Surface((11, 16))
            temp_img.set_colorkey((0, 0, 0))
            temp_img.blit(sheet, (0, 0), (60, i * 20, 16, 16))
            temp = pygame.transform.scale(temp_img, (30, 40))
            self.small_mario.append(temp)

        self.image = self.small_mario[0]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.x_change = 0
        self.y_change = 0

        self.mario_big = False
        self.mario_fire = False
        self.mario_invincible = False

    def update(self):
        self.calc_gravity()

        self.rect.x += self.x_change

        # Checks if Mario collides with a pipe from the sides and prevents him from moving into it
        pipe_collide = pygame.sprite.spritecollide(self, self.pipes, False)
        for pipe in pipe_collide:
            if self.x_change > 0:
                self.rect.right = pipe.rect.left
            if self.x_change < 0:
                self.rect.left = pipe.rect.right

        self.rect.y += self.y_change
        # Checks if Mario collides with a pipe from the top and allows him to stand on it
        pipe_collide = pygame.sprite.spritecollide(self, self.pipes, False)
        for pipe in pipe_collide:
            if self.y_change > 0:
                self.rect.bottom = pipe.rect.top
            elif self.y_change < 0:
                self.rect.top = pipe.rect.bottom
            self.y_change = 0

        #brick_collide = pygame.sprite.spritecollide(self, self.bricks, False)
        #for brick in brick_collide:
        #    if self.x_change > 0:
        #        self.rect.right = brick.rect.left
        #    if self.x_change < 0:
        #        self.rect.left = brick.rect.right

        # Checks collision with the bricks from the top and bottom so that he can stand on them and not go through them
        brick_collide = pygame.sprite.spritecollide(self, self.bricks, False)
        for brick in brick_collide:
            if self.y_change > 0:
                self.rect.bottom = brick.rect.top
            elif self.y_change < 0:
                self.rect.top = brick.rect.bottom
            self.y_change = 0

            # Checks if the brick with the star is hit, if it is then spawns a moving star, and change block to empty
            if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                    and brick.block_type == 5 and not brick.change_brick:
                brick.change_brick = True
                upgrade = Upgrade(self.screen, self.settings, self.pipes, self.bricks,
                                  brick.rect.x, brick.rect.y - 20, 3)
                self.upgrades.add(upgrade)
                brick.change()

            if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                    and brick.block_type == 6 and not brick.change_brick:
                brick.change_brick = True
                upgrade = Upgrade(self.screen, self.settings, self.pipes, self.bricks,
                                  brick.rect.x, brick.rect.y - 20, 2)
                self.upgrades.add(upgrade)
                brick.change()

            # Checks if ? block is hit and if it is check what kind it is
            if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                    and brick.block_type == 2:
                brick.change()
                # Checks if it is a ? block with a mushroom in it and spawns one when hit and change block to empty
                if brick.block_type == 2 and not brick.change_brick and brick.rect.y < self.rect.y \
                        and not self.mario_big:
                    brick.change_brick = True
                    upgrade = Upgrade(self.screen, self.settings, self.pipes, self.bricks,
                                      brick.rect.x, brick.rect.y - 20, 0)
                    self.upgrades.add(upgrade)
                # Checks if Mario is big and if he is then mushroom block spawns a fire flower and change block to empty
                if brick.block_type == 2 and not brick.change_brick and brick.rect.y < self.rect.y \
                        and self.mario_big:
                    brick.change_brick = True
                    upgrade = Upgrade(self.screen, self.settings, self.pipes, self.bricks,
                                      brick.rect.x, brick.rect.y - 40, 1)
                    self.upgrades.add(upgrade)
            # Checks if ? block is regular one and spawns draws a coin for a bit when hit and change block to empty
            if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                    and brick.block_type == 1:
                brick.change()

            # Check if Mario is big and below the block and if he is and hits it the brick is removed
            if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                    and brick.block_type == 0 and self.mario_big:
                self.bricks.remove(brick)

        # Checks if Mario ate the mushroom, fire flower, or star and if he did set the corresponding flag to true
        upgrade_collide = pygame.sprite.spritecollide(self, self.upgrades, True)
        for upgrade in upgrade_collide:
            if upgrade.up_type == 0:
                self.mario_big = True
            if upgrade.up_type == 1 and self.mario_big:
                self.mario_fire = True
            if upgrade.up_type == 1:
                self.stats.lives += 1
            if upgrade.up_type == 3:
                self.mario_invincible = True

    def calc_gravity(self):
        """Calculates gravity and pulls Mario back down after being in the air for a period of time"""
        if self.y_change == 0:
            self.y_change = 1
        else:
            self.y_change += .05
        if self.rect.y >= self.settings.base_level - self.rect.height and self.y_change >= 0:
            self.y_change = 0
            self.rect.y = self.settings.base_level - self.rect.height

    def move_left(self):
        self.x_change = -3

    def move_right(self):
        self.x_change = 3

    def move_stop(self):
        self.x_change = 0

    def move_jump(self):
        self.y_change = -4

    def blitme(self):
        self.screen.blit(self.image, self.rect)
