import pygame
import random
import math
from entities.cell import Cell

BLUE = (0, 76, 153)

class Player(Cell):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.size = 5

        if(pygame.display.get_surface() is not None):
            self.x = pygame.display.get_surface().get_width() / 2
            self.y = pygame.display.get_surface().get_height() / 2

        else:
            self.x = random.randrange(0, 600)
            self.y = random.randrange(0, 600)

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), self.size, 0)

    def update(self):
        pos = pygame.mouse.get_pos()
        relative_x, relative_y = pos[0] - self.x, pos[1] - self.y
        angle = math.atan2(relative_y, relative_x)

        dist_cursor = math.sqrt(pow(pos[0] - self.x, 2) + pow(pos[1] - self.y, 2))

        self.x += math.cos(angle)
        self.y += math.sin(angle)
