import chess
from evaluate import evaluate
from random import choice

class MinimaxBot():   
    def __init__(self, depth):
        self.depth = depth

    def move(self, board):
        board.makeMove(self.minimaxMove(self.depth, board, False))
        
    def minimaxMove(self, depth, board, isMax):
        maxEval = -10000
        bestMoves = []

        for move in board.getLegalMoves():
            board.makeMove(move)
            eval = self.minimax(depth-1, board, -10000, 10000, isMax)
            board.undoMove()

            if eval > maxEval:
                bestMoves.clear()
                bestMoves.append(move)
                maxEval = eval
            elif eval == maxEval:
                bestMoves.append(move)
        
        return choice(bestMoves)
        
    def minimax(self, depth, board, alpha, beta, isMax):
        if depth <= 0:
            return -evaluate(board)

        if isMax:
            maxEval = -10000
            for move in board.getLegalMoves():
                board.makeMove(move)
                maxEval = max(maxEval, self.minimax(depth-1, board, alpha, beta, False))
                board.undoMove()
                alpha = max(alpha, maxEval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = 10000
            for move in board.getLegalMoves():
                board.makeMove(move)
                minEval = min(minEval, self.minimax(depth-1, board, alpha, beta, True))
                board.undoMove()
                beta = min(beta, minEval)
                if beta <= alpha:
                    break
            return minEval
        
    def name(self):
        return f"Minimax Bot({self.depth})"