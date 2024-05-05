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

    # check piece value as base
    value = checkPieceValue(board, color)

    # check for draw and attempt to draw if losing
    value += checkDrawValue(board, value)

    # check for # moves in next position
    #value += checkMobility(board) / 5

    if color == chess.WHITE:
        value += checkAttackingSpaces(board, chess.WHITE) 
        value -= checkAttackingSpaces(board, chess.BLACK) 
    else:
        value -= checkAttackingSpaces(board, chess.WHITE)
        value += checkAttackingSpaces(board, chess.BLACK) 

    # check for control of center
    #value += checkPositioning(board, color) / 2

    return value

def checkPieceValue(board, color):
    value = 0
    for piece in board.getPieces():
        if board.getPieceColor(piece) == color:
            value += board.getPieceValue(piece)
        else:
            value -= board.getPieceValue(piece)
            
    return value

def checkMobility(board):
    return len(board.getLegalMoves())

def checkDrawValue(board, value):
    if board.isDraw():
        if value > 0:
            return -100
        else:
            return 100
    return 0
        
def checkAttackingSpaces(board, color):
    value = 0
    for space in chess.SQUARES:
        if board.isAttackedBy(color, space):
            value += 0.05
    return value

controlMap = [0.8, 1.3, 1.5, 1.7, 1.7, 1.5, 1.3, 0.8,
              0.8, 1.3, 1.4, 2.4, 2.4, 1.4, 1.3, 0.8,
              0.9, 1.0, 2.5, 1.8, 1.8, 2.5, 1.0, 0.9,
              0.9, 1.6, 1.8, 2.8, 2.8, 1.8, 1.6, 0.9,
              0.9, 1.6, 1.8, 2.8, 2.8, 1.8, 1.6, 0.9,
              0.9, 1.0, 2.5, 1.8, 1.8, 2.5, 1.0, 0.9,
              0.8, 1.3, 1.4, 2.4, 2.4, 1.4, 1.3, 0.8,
              0.8, 1.3, 1.5, 1.7, 1.7, 1.5, 1.3, 0.8]

def checkPositioning(board, color):
    value = 0
    for i, space in enumerate(chess.SQUARES):
        spaceColor = board.getColorAt(space)
        if spaceColor == None:
            continue
        elif spaceColor == color:
            value += controlMap[i]
        else:
            value -= controlMap[i]
    return value