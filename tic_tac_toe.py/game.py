import pygame
import sys
import numpy as np
'''https://www.pygame.org/docs/ref/draw.html'''
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
WIN.fill(BG_COLOR)

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# pygame.draw.line(WIN, RED, (10, 10), (300, 300), 10)


def draw_lines():
    pygame.draw.line(WIN, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(WIN, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(WIN, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(WIN, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


'''print(is_board_full())
# marking all squares
for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        if board[row][col] == 0:
            mark_square(row, col, 1)'''

draw_lines()
# Start the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Display the surface
    pygame.display.update()
