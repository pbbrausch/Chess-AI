import math, sys, time, chess
from evaluate import evaluate
from random import choice

class MinimaxBot():   
    def __init__(self, maxDepth):
        self.maxDepth = maxDepth

    def setColor(self, color):
        self.color = color

    def makeMove(self, board):
        if self.color == None:
            sys.exit("Need to set color.")
        
        maxEval = -math.inf
        bestMove = None

        for move in board.getLegalMoves():
            curr = self.minimax(board.copy(), move, 1, True, -math.inf, math.inf)

            if curr > maxEval:
                bestMove = move
                maxEval = curr
        
        board.makeMove(bestMove)
            
    def minimax(self, board, move, depth, maxPlayer, alpha, beta):
        board.makeMove(move)

        #Debug
        #print(f"Depth: {depth}")
        #print(board.toString())
        #time.sleep(1)
        
        if depth == self.maxDepth or board.isDraw():
            return evaluate(board, self.color)
        
        if maxPlayer:
            maxEval = -math.inf
            for nextMove in board.getLegalMoves():
                eval = self.minimax(board.copy(), nextMove, depth+1, False, alpha, beta)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = math.inf
            for nextMove in board.getLegalMoves():
                eval = self.minimax(board.copy(), nextMove, depth+1, True, alpha, beta)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval
        
    def name(self):
        return f"Minimax Bot({self.maxDepth})"