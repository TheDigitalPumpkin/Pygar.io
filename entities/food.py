import pygame
import random
from constants import *
from entities.cell import Cell
from pygame import gfxdraw

class Food(Cell):
    def __init__(self):
        super().__init__()
        self.size = 4
        self.image = pygame.Surface([4, 4])
        #self.image.fill(DARK_GREEN)
        self.rect = self.image.get_rect()
        self.x = random.randrange(0, 1350)
        self.y = random.randrange(0, 760)

    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, self.x, self.y, self.size, DARK_GREEN)
        pygame.gfxdraw.filled_circle(screen, self.x, self.y, self.size, DARK_GREEN)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size
