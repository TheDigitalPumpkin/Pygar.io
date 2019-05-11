import pygame
import random
import math
from pygame import gfxdraw
from constants import *
from entities.cell import Cell
from entities.player import Player

class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.size = 8
        self.directions = [-1, 1, 0, 1, -1]

        self.x = random.randrange(0, 1300)
        self.y = random.randrange(0, 760)

    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), int(self.size), PURPLE)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), int(self.size), PURPLE)

    def distance_from_player(self, player):
        dist = math.sqrt((self.x - player.get_x()) ** 2 + (self.y - player.get_y()) ** 2)
        try:
            x = (player.get_x() - self.x) / dist
            y = (player.get_y() - self.y) / dist
        except ZeroDivisionErorr:
            return False
        return (x, y)

    def update(self, player):
        new_position = self.distance_from_player(player)
        if new_position != 0:
            self.x, self.y = (self.x + new_position[0] / 2, self.y + new_position[1] / 2)
        else:
            self.x = self.directions[random.randrange(0, 4)]
            self.y = self.directions[random.randrange(0, 4)]

    def increase_size(self, size):
        self.size += size / 4

    def decrease_size(self, size):
        self.size -= size / 4
