import pygame

class Cell(pygame.sprite.Sprite):
    def init(self):
        super().__init__()
        self.image = pygame.Surface([2, 2])
        self.rect = self.image.get_rect()
        self.size = 2
        self.x = 0
        self.y = 0
