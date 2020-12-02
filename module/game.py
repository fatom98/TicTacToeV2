import pygame
import random
from .board import Board
from .constants import BLACK
from itertools import cycle
from .ai import Ai


class Game:

    def __init__(self, win):
        self.win = win
        self.again()

    def again(self):
        self.win.fill(BLACK)
        self.board = Board()
        self.pc = Ai()
        self.human = random.choice(["X", "O"])
        self.ai = "X" if self.human == "O" else "O"
        self.end = False
        self.turn = random.choice((self.human, self.ai))
        self.winner = None

        if self.turn == self.ai:
            self.ai_move()

    def update(self):
        self.board.draw_board(self.win)
        pygame.display.update()

    def human_move(self, pos):

        if self.board.get_pos(pos) == "":

            if self.human == "O":
                self.board.draw_o(self.win, pos)
            else:
                self.board.draw_x(self.win, pos)

            self.board.set_board(pos, self.human)
            self.change_turn(self.ai)

    def ai_move(self):

        pos = self.pc.move(self.board)

        if self.board.get_pos(pos) == "":

            if self.ai == "O":
                self.board.draw_o(self.win, pos)
            else:
                self.board.draw_x(self.win, pos)

            self.board.set_board(pos, self.ai)
            self.change_turn(self.human)

    def change_turn(self, next):

        win = self.board.win()

        if win == False:
            self.turn = next

            if self.turn == self.ai:
                self.ai_move()

        else:
            self.finish(win)

    def finish(self, state):
        if state == "tie":
            self.winner = "No body"

        else:
            self.winner = self.turn

        self.end = True
