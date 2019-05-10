import pygame

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 76, 153)
DARK_GREEN = (0, 102, 0)
DARK_RED = (102, 0, 0)
WHITE = (255, 255 , 255)

# Screen dimension
SCREEN_SIZE = [1366, 768]

# Game events
generate_food = pygame.USEREVENT + 1
generate_poison = pygame.USEREVENT + 2
