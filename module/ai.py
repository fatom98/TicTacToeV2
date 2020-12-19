from .board import Board
from copy import deepcopy
from .constants import ROWS, COLS
from math import inf
import random


class Ai:

    def __init__(self, board, human, ai):
        self.board = board
        self.human = human
        self.ai = ai
        print(self.ai, self.human)

        self.scores = {
            self.ai: 10,
            self.human: -10,
            "tie": 0
        }

    def move(self, board):
        brd = deepcopy(board.board)

        if self.board.num_available_spot(brd) == 9:
            return random.choice(self.board.get_available(brd))

        move, score = self.minimax(brd, self.ai)
        return move

    def minimax(self, board, turn):
        end = self.board.win(board, turn)

        if end:
            win = self.ai if end == self.human else self.human
            available = self.board.num_available_spot(board)
            score = self.scores[win] * (available + 1)
            return [-1, score]

        best = [-1, -inf] if turn == self.ai else [-1, inf]
        other = self.human if turn == self.ai else self.ai

        for row, col in self.board.get_available(board):

            board[row][col] = turn
            score = self.minimax(board, other)
            board[row][col] = ""
            score[0] = (row, col)

            if turn == self.ai:
                if best[1] < score[1]:
                    best = score

            else:
                if best[1] > score[1]:
                    best = score

        return best
