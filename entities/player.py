import pygame
import random
import math
from pygame import gfxdraw
from constants import *
from entities.cell import Cell


class Player(Cell):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.size = 8

        if(pygame.display.get_surface() is not None):
            self.x = pygame.display.get_surface().get_width() / 2
            self.y = pygame.display.get_surface().get_height() / 2

        else:
            self.x = random.randrange(0, 600)
            self.y = random.randrange(0, 600)

    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), int(self.size), BLUE)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), int(self.size), BLUE)

    def update(self):
        pos = pygame.mouse.get_pos()
        relative_x, relative_y = pos[0] - self.x, pos[1] - self.y
        angle = math.atan2(relative_y, relative_x)

        dist_cursor = math.sqrt(pow(pos[0] - self.x, 2) + pow(pos[1] - self.y, 2))

        self.x += math.cos(angle)
        self.y += math.sin(angle)

    def increase_size(self, size):
        self.size += size / 4

    def decrease_size(self, size):
        self.size -= size / 4

    def get_size(self):
        return self.size

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
