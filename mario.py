import pygame
from pygame.sprite import Sprite
from upgrade import Upgrade


class Mario(Sprite):

    def __init__(self, screen, settings, pipes, bricks, upgrades, stats, enemies, poles, secret_bricks, secret_pipes):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.pipes = pipes
        self.secret_pipes = secret_pipes
        self.bricks = bricks
        self.secret_bricks = secret_bricks
        self.upgrades = upgrades
        self.enemies = enemies
        self.poles = poles
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
        self.crouch = False

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
        self.x_change = 0
        self.y_change = 0

        self.frame_counter = 0
        self.flash_frame = 0
        self.invinc_length = 0

        # Temp invincibilty
        self.invinc = False

        # if fired is true, shroomed must be true, but can have shroom true and fired false
        # set shroomed and star true for big star mario
        self.dead = False
        self.shroomed = False
        self.fired = False
        self.star_pow = False

        # counts number of coins from the multi coin brick block
        self.count = 0

    def update(self):
        self.invincible()
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
        if self.invinc_length < 600:
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
            self.invinc_length += 1
        else:
            self.star_pow = False
            self.invinc_length = 0

    def update_big_star(self):
        self.move()
        if self.invinc_length < 600:
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
        else:
            self.star_pow = False
            self.invinc_length = 0

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
        # Checks if Mario has collided with the flag pole and has him slowly move down the pole
        if pygame.sprite.spritecollide(self, self.poles, False):
            self.stats.reached_pole = True
            if self.rect.y != 508:
                self.rect.y += 1
            self.rect.x += self.x_change
        else:
            self.calc_gravity()

            if self.rect.left > 20:
                self.rect.x += self.x_change
            else:
                self.rect.x = 22
            # Checks if Mario is in the main level
            if not self.stats.secret_level:
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
                        if pipe.num == 3 and self.crouch:
                            self.stats.activate_secret = True
                            self.stats.secret_level = True
                    elif self.y_change < 0:
                        self.rect.top = pipe.rect.bottom
                    self.y_change = 0

                # Checks if Mario collides with side of bricks
                brick_collide = pygame.sprite.spritecollide(self, self.bricks, False)
                for brick in brick_collide:
                    if self.rect.right >= brick.rect.left and brick.rect.bottom == self.rect.bottom:
                        self.x_change = 0
                    if self.rect.left <= brick.rect.right and brick.rect.bottom == self.rect.bottom:
                        self.x_change = 0

                # Checks collision with the bricks from the top and
                # bottom so that he can stand on them and not go through them
                brick_collide = pygame.sprite.spritecollide(self, self.bricks, False)
                for brick in brick_collide:
                    if self.y_change > 0:
                        self.rect.bottom = brick.rect.top
                    elif self.y_change < 0:
                        self.rect.top = brick.rect.bottom
                    self.y_change = 0

                    # Checks if the brick with the star is hit,
                    # if it is then spawns a moving star, and change block to empty
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
                        # Checks if it is a ? block with a mushroom in it
                        # and spawns one when hit and change block to empty
                        if brick.block_type == 2 and not brick.change_brick and brick.rect.y < self.rect.y \
                                and not self.shroomed:
                            brick.change_brick = True
                            upgrade = Upgrade(self.screen, self.settings, self.pipes, self.bricks,
                                              brick.rect.x, brick.rect.y - 20, 0)
                            self.upgrades.add(upgrade)
                        # Checks if Mario is big and if he is then mushroom block
                        # spawns a fire flower and change block to empty
                        if brick.block_type == 2 and not brick.change_brick and brick.rect.y < self.rect.y \
                                and self.shroomed:
                            brick.change_brick = True
                            upgrade = Upgrade(self.screen, self.settings, self.pipes, self.bricks,
                                              brick.rect.x, brick.rect.y - 40, 1)
                            self.upgrades.add(upgrade)
                    # Checks if ? block is regular one and spawns draws a coin for
                    # a bit when hit and change block to empty
                    if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                            and brick.block_type == 1:
                        brick.change()
                        self.stats.coins += 1

                    if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                            and brick.block_type == 9 and not brick.change_brick:
                        if self.count != 4:
                            self.stats.coins += 1
                            self.count += 1
                        else:
                            brick.change_brick = True
                            brick.change()

                    # Check if Mario is big and below the block and if he is and hits it the brick is removed
                    if brick.rect.x - 20 < self.rect.x < brick.rect.x + 20 and brick.rect.y < self.rect.y \
                            and brick.block_type == 0 and self.shroomed:
                        self.bricks.remove(brick)
            # Checks if Mario is in the underground chamber
            if self.stats.secret_level:
                # If Mario collides with the side prevents him from going through
                pipe_collide = pygame.sprite.spritecollide(self, self.secret_pipes, False)
                for pipe in pipe_collide:
                    if self.x_change > 0:
                        self.rect.right = pipe.rect.left
                        # If Mario collides with a certain part of the pipe the secret level is cleared and
                        # Mario returns to the main level
                        if pipe.num == 7:
                            self.secret_pipes.empty()
                            self.upgrades.empty()
                            self.secret_bricks.empty()
                            self.stats.activate_main_lvl = True
                            self.stats.main_level = True
                            self.stats.return_main_level = True
                            self.stats.secret_level = False
                    if self.x_change < 0:
                        self.rect.left = pipe.rect.right

                self.rect.y += self.y_change

                # Checks if Mario collides with a pipe from the top and allows him to stand on it
                pipe_collide = pygame.sprite.spritecollide(self, self.secret_pipes, False)
                for pipe in pipe_collide:
                    if self.y_change > 0:
                        self.rect.bottom = pipe.rect.top
                    elif self.y_change < 0:
                        self.rect.top = pipe.rect.bottom
                    self.y_change = 0

                brick_collide = pygame.sprite.spritecollide(self, self.secret_bricks, False)
                for brick in brick_collide:
                    if self.rect.right >= brick.rect.left and brick.rect.bottom == self.rect.bottom:
                        self.x_change = 0
                    if self.rect.left <= brick.rect.right and brick.rect.bottom == self.rect.bottom:
                        self.x_change = 0

                # Checks collision with the bricks from the top and
                # bottom so that he can stand on them and not go through them
                brick_collide = pygame.sprite.spritecollide(self, self.secret_bricks, False)
                for brick in brick_collide:
                    if self.y_change > 0:
                        self.rect.bottom = brick.rect.top
                    elif self.y_change < 0:
                        self.rect.top = brick.rect.bottom
                    self.y_change = 0

            # Checks if Mario ate the mushroom, fire flower, or star and if he did set the corresponding flag to true
            upgrade_collide = pygame.sprite.spritecollide(self, self.upgrades, True)
            for upgrade in upgrade_collide:
                if upgrade.up_type == 0:
                    self.shroomed = True
                if upgrade.up_type == 1 and self.shroomed:
                    self.fired = True
                    self.shroomed = False
                if upgrade.up_type == 1:
                    self.stats.lives += 1
                if upgrade.up_type == 3:
                    self.star_pow = True
                if upgrade.up_type == 4:
                    self.stats.coins += 1
                    self.stats.score += 200

            enemy_collide = pygame.sprite.spritecollide(self, self.enemies, False)
            for enemy in enemy_collide:
                if self.star_pow:
                    self.enemies.remove(enemy)
                if enemy.rect.y > self.rect.y and enemy.enemy_type == 0 and not self.star_pow and not self.invinc:
                    self.enemies.remove(enemy)
                # Transforms Koopa into shell
                if enemy.rect.y > self.rect.y and enemy.enemy_type == 1 and not self.star_pow and not self.invinc:
                    enemy.stunned = True
                # Makes shell move when in contact with it
                if enemy.enemy_type == 1 and enemy.stunned and not self.star_pow:
                    enemy.kicked = True
                if enemy.enemy_type == 0 and enemy.rect.y <= self.rect.y and not self.star_pow and not self.shroomed \
                        and not self.invinc:
                    self.dead = True
                if enemy.rect.y <= self.rect.y and self.shroomed:
                    self.shroomed = False
                    self.invinc = True
                if enemy.rect.y <= self.rect.y and self.fired:
                    self.fired = False
                    self.invinc = True

    def invincible(self):
        """Temporary invinciblity for big or fire Mario after being hit"""
        if self.invinc_length < 100 and self.invinc:
            self.invinc_length += 1
        else:
            self.invinc = False
            self.invinc_length = 0

    def calc_gravity(self):
        """Calculates gravity and pulls Mario back down after being in the air for a period of time"""
        if self.y_change == 0:
            self.y_change = 1
        else:
            self.y_change += .1

    def move_left(self):
        if self.rect.left <= 20:
            self.x_change = 0
        else:
            self.x_change = -3
        self.moving_left = True
        self.facing_right = False

    def move_right(self):
        # self.x_change = 1
        self.x_change = 3
        self.moving_right = True
        self.facing_right = True

    def move_stop(self):
        self.x_change = 0
        self.moving_left = False
        self.moving_right = False

    def move_jump(self):
        self.y_change = -6
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
