import pygame
from imagerect import ImageRect


class Maze:

    def __init__(self, screen):
        self.screen = screen
        self.filename = 'images/level_loc.txt'
        self.shift_world = 0
        self.rect = 500

        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        # for bricks
        self.bricks = []
        self.brick = ImageRect(screen, 'images/bricks/Red_Brick.png', 32, 32)

        self.build()

    def build(self):
        r = self.brick.rect
        w, h = r.width, r.height

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * 32, nrow * 32, w, h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)