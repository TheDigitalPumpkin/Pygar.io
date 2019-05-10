import pygame
import random
from constants import *
from entities.cell import Cell

class Food(Cell):
    def __init__(self):
        super().__init__()
        self.size = 2
        self.image = pygame.Surface([2, 2])
        self.image.fill(DARK_GREEN)
        self.rect = self.image.get_rect()
        self.x = random.randrange(760)
        self.y = random.randrange(1000)

    def draw(self, screen):
        pygame.draw.circle(screen, DARK_GREEN, (self.x, self.y), self.size, 0)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size

    def get_rect(self):
        return self.rect
