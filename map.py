from brick import Brick
from goomba import Goomba
from koopa import Koopa


class Map:
    """Implements Maze"""
    BRICK_SIZE = 40

    def __init__(self, screen, settings, bricks, pipes, enemies, mapfile):
        self.screen = screen
        self.settings = settings
        self.bricks = bricks
        self.pipes = pipes
        self.enemies = enemies
        self.filename = mapfile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.brick = None
        self.goomba = None
        self.koopa = None
        self.deltax = self.deltay = Map.BRICK_SIZE

    def __str__(self): return 'map(' + self.filename + ')'

    def build_brick(self):
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'B':
                    Map.create_brick(self, ncol*dx, nrow*dy, 0)
                if col == '?':
                    Map.create_brick(self, ncol * dx, nrow * dy, 1)
                if col == 'X':
                    Map.create_brick(self, ncol * dx, nrow * dy, 3)
                if col == 'M':
                    Map.create_brick(self, ncol * dx, nrow * dy, 2)
                if col == 'R':
                    Map.create_brick(self, ncol * dx, nrow * dy, 4)
                if col == 'S':
                    Map.create_brick(self, ncol*dx, nrow*dy, 5)
                if col == 'I':
                    Map.create_brick(self, ncol*dx, nrow*dy, 6)
                if col == 'G':
                    Map.create_enemy(self, ncol*dx, nrow*dy, 0)
                if col == 'K':
                    Map.create_enemy(self, ncol*dx, nrow*dy, 1)

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)

    def create_brick(self, x, y, num):
        self.brick = Brick(self.screen, self.settings, num)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.bricks.add(self.brick)

    def create_enemy(self, x, y, num):
        if num == 0:
            self.goomba = Goomba(self.screen, self.settings, self.pipes, self.bricks)
            self.goomba.rect.x = x
            self.goomba.rect.y = y
            self.enemies.add(self.goomba)
        if num == 1:
            self.koopa = Koopa(self.screen, self.settings, self.pipes, self.bricks)
            self.koopa.rect.x = x
            self.koopa.rect.y = y
            self.enemies.add(self.koopa)
