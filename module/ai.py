from .board import Board


class Ai:

    def move(self, board):
        available = board.get_available()
        return available[0]

    @staticmethod
    def minimax():
        pass
