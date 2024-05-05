import math
import chess

# returns value of input board
def evaluate(board, color):

    #check for checkmake
    outcome = board.outcome()
    if outcome:
        if outcome.winner == color:
            return math.inf
        else:
            return -math.inf
        
    # check for draw
    if board.isDraw():
        if value > 0:
            return -math.inf 
        else:
            return math.inf

    # check piece value as base
    value = checkPieceValue(board, color)

    # check for # moves in next position
    #value += checkMobility(board) / 5

    #if color == chess.WHITE:
    #    value += checkAttackingSpaces(board, chess.WHITE) 
    #    value -= checkAttackingSpaces(board, chess.BLACK) 
    #else:
    #    value -= checkAttackingSpaces(board, chess.WHITE)
    #    value += checkAttackingSpaces(board, chess.BLACK) 

    # check for control of center
    value += checkPositioning(board, color)

    return value

def checkPieceValue(board, color):
    value = 0
    for piece in board.getPieces():
        if board.getPieceColor(piece) == color:
            value += board.getPieceValue(piece) * 50
        else:
            value -= board.getPieceValue(piece) * 50
            
    return value

def checkMobility(board):
    return len(board.getLegalMoves())
        
def checkAttackingSpaces(board, color):
    value = 0
    for space in chess.SQUARES:
        if board.isAttackedBy(color, space):
            value += 5
    return value

controlMap = [5, 10, 10, 10, 10, 10, 10, 5,
              5, 10, 10, 30, 30, 10, 10, 5,
              5, 10, 30, 20, 20, 30, 10, 5,
              5, 10, 10, 50, 50, 10, 10, 5,
              5, 10, 10, 50, 50, 10, 10, 5,
              5, 10, 30, 20, 20, 30, 10, 5,
              5, 10, 10, 30, 30, 10, 10, 5,
              5, 10, 10, 10, 10, 10, 10, 5]

def checkPositioning(board, color):
    value = 0
    for (i, space) in enumerate(chess.SQUARES):
        spaceColor = board.getColorAt(space)
        if spaceColor == color:
            value += controlMap[i]
        else:
            value -= controlMap[i]
        
    return value