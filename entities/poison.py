from entities.cell import Cell
from constants import *
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
        pygame.draw.circle(screen, DARK_RED, (int(self.x), int(self.y)), int(self.size), 0)
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), int(self.size / 2), 0)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size
