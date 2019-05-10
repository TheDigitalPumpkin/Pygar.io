import sys, pygame
from player import Player
from food import Food
import random
pygame.init()

SCREEN_SIZE = [1024, 768]
WHITE = (255, 255 , 255)
generate_food = pygame.USEREVENT + 1

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)
pygame.display.set_caption("Pygar.io")

player = Player()
food_list = []

## TODO: Make a separate GameScreen class.
## TODO: Make a list of constants

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == generate_food:
            food_x = random.randrange(0, 760)
            food_y = random.randrange(0, 1000)
            food_list.append(Food(food_x, food_y))
            print(len(food_list))

    pygame.time.set_timer(generate_food, 200)
    screen.fill(WHITE)

    for f in food_list:
        f.draw(screen)

    player.update()
    player.draw(screen)
    pygame.display.flip()
