import pygame
import sys
'''https://www.pygame.org/docs/ref/draw.html'''
from pygame.locals import *

pygame.init()

DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Name of Game")

# Start the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw on the surface object
    DISPLAYSURF.fill((255, 255, 254))
    # Display the surface
    pygame.display.update()
