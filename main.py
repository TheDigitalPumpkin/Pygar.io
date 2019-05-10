import sys, pygame
from entities.player import Player
from entities.food import Food
from entities.poison import Poison
from entities.enemy import Enemy
from constants import *
import random
import math
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()
screen.fill(WHITE)
pygame.display.set_caption("Pygar.io")

player = Player()
food = []
poison = []
enemies = []
score = 0
pygame.time.set_timer(generate_food, 600)
pygame.time.set_timer(generate_poison, 1200)
pygame.time.set_timer(increase_score, 200)

for i in range(0, 4):
    enemies.append(Enemy())

    ## TODO: Make a separate GameScreen class.

def is_colliding(player, cell):
    dist = math.sqrt( ((player.get_x() - cell.get_x()) ** 2) + ((player.get_y() - cell.get_y()) ** 2))
    if(dist < (player.get_size() + cell.get_size() - 1) / 2):
        return True
    else:
        return False

## TODO: Move this to GameScreen class

pygame.font.init()
font = pygame.font.SysFont("Inconsolata", 36)
textSurface = font.render(str(score), True, BLACK)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == generate_food:
            food.append(Food())
            pygame.time.set_timer(generate_food, 600)
        if event.type == generate_poison:
            poison.append(Poison())
            pygame.time.set_timer(generate_poison, 1200)
        if event.type == increase_score:
            score += player.get_size() / 10 + 1

    screen.fill(WHITE)
    textSurface = font.render(str(int(score)), True, BLACK)
    screen_surface = pygame.display.get_surface()
    screen_surface.blit(textSurface, (5, 5))

    for f in food:
        f.draw(screen)

    for p in poison:
        p.draw(screen)

    for f in food:
        for enemy in enemies:
            if(is_colliding(enemy, f)):
                enemy.increase_size(f.get_size())
                food.remove(f)

        if(is_colliding(player, f)):
            player.increase_size(f.get_size())
            food.remove(f)

    for p in poison:
        for enemy in enemies:
            if(is_colliding(enemy, p)):
                enemy.decrease_size(p.get_size())
                poison.remove(p)

        if(is_colliding(player, p)):
            player.decrease_size(p.get_size())
            poison.remove(p)

    for enemy in enemies:
        enemy.update(player)
        enemy.draw(screen)

    player.update()
    player.draw(screen)
    pygame.display.flip()
