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

    @staticmethod
    def get_available(board):

        available = []

        for row in range(ROWS):
            for col in range(COLS):

                if board[row][col] == "":
                    available.append((row, col))

        return available

    @staticmethod
    def num_available_spot(board):
        return len(Board.get_available(board))

    def get_pos(self, pos):
        return self.board[pos[0]][pos[1]]

    def win(self, board, turn):

        if (board[0][0] == board[0][1] == board[0][2] != "" or
            board[1][0] == board[1][1] == board[1][2] != "" or
            board[2][0] == board[2][1] == board[2][2] != "" or
            board[0][0] == board[1][0] == board[2][0] != "" or
            board[0][1] == board[1][1] == board[2][1] != "" or
            board[0][2] == board[1][2] == board[2][2] != "" or
            board[0][0] == board[1][1] == board[2][2] != "" or
                board[0][2] == board[1][1] == board[2][0] != ""):

            return turn

        elif Board.num_available_spot(board) == 0:
            return "tie"

        else:
            return False
