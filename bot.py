from random import choice
import sys

class Bot():    

    def makeMove(self, board):

        if (len(list(board.getLegalMoves())) == 0):
            return False

        board.makeMove(choice(list(board.getLegalMoves())))
        return True