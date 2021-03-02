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
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

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


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(
                    WIN, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(WIN, CROSS_COLOR, (col * 200 + SPACE, row *
                                                    200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(WIN, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


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


def check_win(player):
    # vertical line
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # horizontal line
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # desc diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(WIN, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(WIN, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(WIN, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(WIN, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    WIN.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


'''print(is_board_full())
# marking all squares
for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        if board[row][col] == 0:
            mark_square(row, col, 1)'''

draw_lines()

player = 1
game_over = False
# Start the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x corrdinate
            mouseY = event.pos[1]  # y coordinate

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
    # Display the surface
    pygame.display.update()
