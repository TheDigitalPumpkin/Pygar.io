import sys, pygame
from entities.player import Player
from entities.food import Food
from constants import *
import random
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)
pygame.display.set_caption("Pygar.io")

player = Player()
food_list = []
pygame.time.set_timer(generate_food, 400)

## TODO: Make a separate GameScreen class.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == generate_food:
            food_x = random.randrange(0, 760)
            food_y = random.randrange(0, 1000)
            food_list.append(Food(food_x, food_y))
            pygame.time.set_timer(generate_food, 400)

    screen.fill(WHITE)

    for f in food_list:
        f.draw(screen)

    player.update()
    player.draw(screen)
    pygame.display.flip()
