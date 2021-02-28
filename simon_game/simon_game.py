import pygame
import sys

from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
LIME = (0, 255, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simon Says")

# Start the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    '''pygame.draw.polygon(WIN, GREEN, ((146, 0),
                                     (291, 106), (236, 277), (56, 277), (0, 106)))'''
    pygame.draw.rect(WIN, PURPLE, (237.5, 87.5, 200, 200))
    pygame.draw.rect(WIN, BLUE, (462.5, 87.5, 200, 200))
    pygame.draw.rect(WIN, GREEN, (237.5, 312.5, 200, 200))
    pygame.draw.rect(WIN, RED, (462.5, 312.5, 200, 200))
    '''fontObj = pygame.font.SysFont(
        'tahoma', 30, bold=False, italic=False)
    fontSurfaceObject = fontObj.render("This is my message", True, WHITE, BLUE)
    DISPLAYSURF.blit(fontSurfaceObject, (10, 10))'''
    '''game = pygame.Surface((700, 500))
    game.fill(WHITE)
    DISPLAYSURF.blit(game, (100, 50))'''

    # Display the surface
    pygame.display.update()
