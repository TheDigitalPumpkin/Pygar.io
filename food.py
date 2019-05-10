import pygame
import random
from cell import Cell

DARK_GREEN = (0, 102, 0)

class Food(Cell):
    def __init__(self, x, y):
        super().__init__()
        self.size = 2
        self.image = pygame.Surface([2, 2])
        self.image.fill(DARK_GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, DARK_GREEN, (self.x, self.y), self.size, 0)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
