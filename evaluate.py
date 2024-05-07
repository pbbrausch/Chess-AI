import math
import chess

# returns value of input board
def evaluate(board):

    #get piece value
    value = checkPieceValue(board)

    #check for outcome
    outcome = board.outcome()
    if outcome:
        # check for checkmate
        if outcome.winner == chess.WHITE:
            return math.inf
        else:
            return -math.inf

    return value

def checkPieceValue(board):
    value = 0
    for piece in board.getPieces():
        c = board.getPieceColor(piece)
        if c == chess.WHITE:
            value += board.getPieceValue(piece)
        elif c == chess.BLACK:
            value -= board.getPieceValue(piece)
            
    return value