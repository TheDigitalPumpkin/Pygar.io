import sys, pygame
from entities.player import Player
from entities.food import Food
from constants import *
import random
import math
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)
pygame.display.set_caption("Pygar.io")

player = Player()
food_list = []
food_rect_list = []
pygame.time.set_timer(generate_food, 400)

## TODO: Make a separate GameScreen class.

def is_colliding(player, cell):
    dist = math.sqrt( ((player.get_x() - cell.get_x()) ** 2) + ((player.get_y() - cell.get_y()) ** 2))
    if(dist < (player.get_size() + cell.get_size() - 1) / 2):
        return True
    else:
        return False



# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == generate_food:
            new_food = Food()
            food_list.append(new_food)
            pygame.time.set_timer(generate_food, 600)

    screen.fill(WHITE)

    for f in food_list:
        f.draw(screen)

    for f in food_list:
        if(is_colliding(player, f)):
            player.increase_size(f.get_size())
            food_list.remove(f)

    player.update()
    player.draw(screen)
    pygame.display.flip()
