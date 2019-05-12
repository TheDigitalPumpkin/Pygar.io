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

    # Draws the player's current score on the top left corner of the screen.
    screen.fill(WHITE)
    textSurface = font.render(str(int(score)), True, BLACK)
    screen_surface = pygame.display.get_surface()
    screen_surface.blit(textSurface, (5, 5))

    # The following 2 loops draw the food and poison cells on the screen if theyy are active. If they aren't active, removes them from the arrays.
    for f in food:
        if f.is_active():
            f.draw(screen)
        else:
            food.remove(f)

    for p in poison:
        if p.is_active():
            p.draw(screen)
        else:
            poison.remove(p)

    # The following 2 loops handle the player's and the enemies' colision with food and poison cells.
    for f in food:
        # For each enemy
        for enemy in enemies:
            # Checks if the enemy is colliding with a food cell
            if(is_colliding(enemy, f)):
                # If it is, increases the enemy's size and deactivates the food cell
                enemy.increase_size(f.get_size())
                f.deactivate()

        # If the player is colliding with a food cell, increases the player's size and deactivates the food cell.
        if(is_colliding(player, f)):
            player.increase_size(f.get_size())
            f.deactivate()

    # Same as the loop before, but deacreses the enemy's or player's size, sicne it's a poison cell.
    for p in poison:
        for enemy in enemies:
            if(is_colliding(enemy, p)):
                enemy.decrease_size(p.get_size())
                p.deactivate()

        if(is_colliding(player, p)):
            player.decrease_size(p.get_size())
            p.deactivate()

    for enemy in enemies:
        enemy.update(player)
        enemy.draw(screen)

    # Updates the player's position, then draws the player on the screen.
    player.update()
    player.draw(screen)
    pygame.display.flip()
