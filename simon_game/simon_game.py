import pygame
import sys

from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
LIGHTBLUE = (0, 0, 254)
GREEN = (0, 128, 0)
LIGHTGREEN = (0, 204, 0)
RED = (178, 0, 0)
LIGHTRED = (255, 0, 0)
PURPLE = (128, 0, 128)
LIGHTPURPLE = (192, 128, 192)
YELLOW = (255, 255, 0)
LIME = (0, 255, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simon Says")

# Start the main game loop
while True:
    button1 = pygame.draw.rect(WIN, PURPLE, (237.5, 87.5, 200, 200))
    button2 = pygame.draw.rect(WIN, BLUE, (462.5, 87.5, 200, 200))
    button3 = pygame.draw.rect(WIN, GREEN, (237.5, 312.5, 200, 200))
    button4 = pygame.draw.rect(WIN, RED, (462.5, 312.5, 200, 200))
    # Handle events
    '''def getClicked(mouse_pos):
        pygame.draw.rect(WIN, WHITE, (237.5, 87.5, 200, 200))'''

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            if button1.collidepoint((mousex, mousey)):
                pygame.draw.rect(WIN, LIGHTPURPLE, (237.5, 87.5, 200, 200))
            if button2.collidepoint((mousex, mousey)):
                pygame.draw.rect(WIN, LIGHTBLUE, (462.5, 87.5, 200, 200))
            if button3.collidepoint((mousex, mousey)):
                pygame.draw.rect(WIN, LIGHTGREEN, (237.5, 312.5, 200, 200))
            if button4.collidepoint((mousex, mousey)):
                pygame.draw.rect(WIN, LIGHTRED, (462.5, 312.5, 200, 200))
                #blink = pygame.draw.rect(WIN, WHITE, (237.5, 87.5, 200, 200))
                #pygame.time.set_timer(blink, 1000)
                '''pygame.time.delay(10)'''
                #mouse = pygame.mouse.get_pos()
                # getClicked(mouse)
    '''pygame.draw.polygon(WIN, GREEN, ((146, 0),
                                     (291, 106), (236, 277), (56, 277), (0, 106)))'''
    '''fontObj = pygame.font.SysFont(
        'tahoma', 30, bold=False, italic=False)
    fontSurfaceObject = fontObj.render("This is my message", True, WHITE, BLUE)
    DISPLAYSURF.blit(fontSurfaceObject, (10, 10))'''
    '''game = pygame.Surface((700, 500))
    game.fill(WHITE)
    DISPLAYSURF.blit(game, (100, 50))'''

    # Display the surface
    pygame.display.update()
