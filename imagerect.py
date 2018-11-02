import pygame


class ImageRect:
    def __init__(self, screen, imagename, height, width):
        self.screen = screen
        # self.name = 'images/' + imagename + '.png'
        self.img = pygame.image.load(imagename)
        self.img = pygame.transform.scale(self.img, (height, width))
        self.rect = self.img.get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.image = self.img

    def __str__(self):
        return 'imagerect(' + str(self.image) + str(self.rect) + ')'

    def blitme(self):
        self.screen.blit(self.image, self.rect)