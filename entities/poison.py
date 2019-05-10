from entities.cell import Cell
from constants import *
from pygame import gfxdraw
import random
import pygame


class Poison(Cell):
    def __init__(self):
        self.size = random.randrange(4, 12)
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(DARK_RED)
        self.rect = self.image.get_rect()
        self.x = random.randrange(0, 1350)
        self.y = random.randrange(0, 760)

    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), int(self.size), DARK_RED)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), int(self.size), DARK_RED)
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), int(self.size / 2), BLACK)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), int(self.size / 2), BLACK)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size
