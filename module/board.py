import pygame
from .constants import WHITE, BLACK, ROWS, COLS, SQUARE_SIZE, WIDTH, HEIGHT, PADDING


class Board:

    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):

        for row in range(ROWS):
            self.board.append([])

            for col in range(COLS):
                self.board[row].append("")

    def draw_board(self, win):

        for row in range(ROWS - 1):
            pygame.draw.line(win, WHITE, (PADDING, SQUARE_SIZE * (row + 1)), (WIDTH - PADDING, SQUARE_SIZE * (row + 1)), 3)

        for col in range(COLS - 1):
            pygame.draw.line(win, WHITE, (SQUARE_SIZE * (col + 1), PADDING), (SQUARE_SIZE * (col + 1), HEIGHT - PADDING), 3)

    def draw_x(self, win, pos: tuple):
        x = pos[0] * SQUARE_SIZE + PADDING
        y = pos[1] * SQUARE_SIZE + PADDING
        pygame.draw.line(win, WHITE, (x, y), (x + (SQUARE_SIZE - 2 * PADDING), y + (SQUARE_SIZE - 2 * PADDING)), 3)
        pygame.draw.line(win, WHITE, (x + (SQUARE_SIZE - 2 * PADDING), y), (x, y + (SQUARE_SIZE - 2 * PADDING)), 3)

    def draw_o(self, win, pos: tuple):
        x = pos[0] * SQUARE_SIZE + SQUARE_SIZE//2
        y = pos[1] * SQUARE_SIZE + SQUARE_SIZE//2
        pygame.draw.circle(win, WHITE, (x, y), SQUARE_SIZE//2 - PADDING)
        pygame.draw.circle(win, BLACK, (x, y), SQUARE_SIZE//2 - PADDING - 5)

    def set_board(self, pos: tuple, piece: str):
        r, c = pos
        self.board[r][c] = piece

    def get_available(self):

        available = []

        for row in range(ROWS):
            for col in range(COLS):

                if self.board[row][col] == "":
                    available.append((row, col))

        return available

    def get_pos(self, pos):
        return self.board[pos[0]][pos[1]]

    def win(self):

        if (self.board[0][0] == self.board[0][1] == self.board[0][2] != "" or
            self.board[1][0] == self.board[1][1] == self.board[1][2] != "" or
            self.board[2][0] == self.board[2][1] == self.board[2][2] != "" or
            self.board[0][0] == self.board[1][0] == self.board[2][0] != "" or
            self.board[0][1] == self.board[1][1] == self.board[2][1] != "" or
            self.board[0][2] == self.board[1][2] == self.board[2][2] != "" or
            self.board[0][0] == self.board[1][1] == self.board[2][2] != "" or
                self.board[0][2] == self.board[1][1] == self.board[2][0] != ""):

            return True

        elif len(self.get_available()) == 0:
            print("tie")
            return "tie"

        else:
            return False
