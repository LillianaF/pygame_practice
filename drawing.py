import pygame
import sys
'''https://www.pygame.org/docs/ref/draw.html'''
from pygame.locals import *

pygame.init()

DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
LIME = (0, 255, 0)

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
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, BLUE, (450, 125), 100)
    pygame.draw.circle(DISPLAYSURF, LIME, (450, 175), 100)
    pygame.draw.circle(DISPLAYSURF, PURPLE, (450, 225), 100)
    pygame.draw.polygon(DISPLAYSURF, YELLOW,
                        ((350, 242), (550, 242), (450, 500)))
    '''pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0),
                                             (291, 106), (236, 277), (56, 277), (0, 106)))
    pygame.draw.line(DISPLAYSURF, BLUE, [60, 60], [120, 60], 4)
    pygame.draw.line(DISPLAYSURF, BLUE, [120, 60], [60, 120], 4)
    pygame.draw.line(DISPLAYSURF, BLUE, [60, 120], [120, 120], 4)
    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20)
    pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
    pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))'''

    # Display the surface
    pygame.display.update()
