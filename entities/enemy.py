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
        self.dist_from_player = 10000
        self.directions = [-2, 0, 2]

        self.x = random.randrange(0, 1300)
        self.y = random.randrange(0, 760)

    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), int(self.size), PURPLE)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), int(self.size), PURPLE)

    def distance_from_player(self, player):
        dist = math.sqrt((self.x - player.get_x()) ** 2 + (self.y - player.get_y()) ** 2)
        self.dist_from_player = dist
        try:
            x = (player.get_x() - self.x) / dist
            y = (player.get_y() - self.y) / dist
        except ZeroDivisionErorr:
            return False
        return (x, y)

    def get_distance_from_food(self, food_list):
        dist_food = {}
        for i in range(0, len(food_list)):
            dist = math.sqrt((self.x - food_list[i].get_x()) ** 2 + (self.y - food_list[i].get_y()) ** 2)
            dist_food[dist] = food_list[i]

        sorted(dist_food)
        return dist_food

    def update(self, player, food_dist_list):
        new_position = self.distance_from_player(player)

        ## TODO: Fix crashing when dealing with multiple AI
        if new_position != 0 and self.dist_from_player <= 200:
            self.x, self.y = (self.x + new_position[0] / 2, self.y + new_position[1] / 2)
        else:
            nearest_food = food_dist_list[list(food_dist_list.keys())[0]]
            relative_x, relative_y = nearest_food.get_x() - self.x, nearest_food.get_y() - self.y
            angle = math.atan2(relative_y, relative_x)
            self.x += math.cos(angle)
            self.y += math.sin(angle)

    def increase_size(self, size):
        self.size += size / 4

    def decrease_size(self, size):
        self.size -= size / 4
