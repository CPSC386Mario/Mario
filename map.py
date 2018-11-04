from brick import Brick


class Map:
    """Implements Maze"""
    BRICK_SIZE = 40

    def __init__(self, screen, settings, bricks, mapfile):
        self.screen = screen
        self.settings = settings
        self.bricks = bricks
        self.filename = mapfile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.brick = None
        self.deltax = self.deltay = Map.BRICK_SIZE

    def __str__(self): return 'map(' + self.filename + ')'

    def build_brick(self):
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'B':
                    Map.create_brick(self, ncol*dx, nrow*dy)
                if col == '?':
                    Map.create_item_brick(self, ncol * dx, nrow * dy, 1)
                if col == 'X':
                    Map.create_bottom_brick(self, ncol * dx, nrow * dy)
                if col == 'M':
                    Map.create_item_brick(self, ncol * dx, nrow * dy, 2)
                if col == 'R':
                    Map.create_stair_brick(self, ncol * dx, nrow * dy)

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)

    def create_brick(self, x, y):
        self.brick = Brick(self.screen, self.settings, 0)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.bricks.add(self.brick)

    def create_item_brick(self, x, y, num):
        self.brick = Brick(self.screen, self.settings, num)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.bricks.add(self.brick)

    def create_bottom_brick(self, x, y):
        self.brick = Brick(self.screen, self.settings, 3)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.bricks.add(self.brick)

    def create_stair_brick(self, x, y):
        self.brick = Brick(self.screen, self.settings, 4)
        self.brick.rect.x = x
        self.brick.rect.y = y
        self.bricks.add(self.brick)
