import math
import chess
import numpy as np

class Board:
    def __init__(self, board=None):

        if board != None:
            self.board = board
        else:
            self.board = chess.Board()
    
    def getLegalMoves(self): #returns a list of all legal moves
        return list(self.board.legal_moves)
    
    def makeMove(self, move): #makes a move if legal ex "e4"
        if move in self.board.legal_moves:
            self.board.push(move)
        else:
            print("Move Illegal.")
            return False
        return True

    def undoMove(self): #undo's last move
        self.board.pop()

    def getLastMove(self):
        self.board.peek()

    def printBoard(self):
        print(self.board)
        
    def isStalemate(self):
        return self.board.is_stalemate()
    
    def isCheckmate(self):
        return self.board.is_checkmate()
    
    def isInsufficientMaterials(self):
        return self.board.is_insufficient_material()
    
    def isDraw(self):
        return self.isCheckmate() or self.isInsufficientMaterials() or self.isStalemate()

    def isCheck(self):
        return self.board.is_check()
    
    def isAttackedBy(self, color, space): #check if color is attacking space ex (chess.WHITE, chess.E8) - (is white attacking E8)
        return self.board.is_attacked_by(color, space)
    
    def getAllAttackers(self, color, space): #get all pieces color is attacking space with
        return self.board.attackers(color, space)
    
    def canDoThreefoldRepitionDraw(self):
        return self.board.can_claim_threefold_repetition()

    def canDoFiftyMoveDraw(self):
        return self.board.can_claim_fifty_moves()

    def canDraw(self):
        return self.board.can_claim_draw()

    def outcome(self):
        return self.board.outcome()
    
    def reset(self):
        self.board.reset()

    def copy(self):
        return Board(self.board.copy())
    
    def toString(self):
        return str(self.board)
    
    def toArray(self):
        return np.array(list(self.toString().replace(' ', '').replace('\n', '')))
    
    def to2DArray(self):
        return self.to1DArray().reshape(8,8)
    
    def getPieces(self):
        return np.array(list(self.toString().replace(' ', '').replace('\n', '').replace('.', '')))
    
    def getPieceColor(self, letter):
        if (letter.isupper()):
            return chess.WHITE
        
        return chess.BLACK
    
    def getColorAt(self, square):
        return self.board.color_at(square)

    def getPieceValue(self, letter):
        match letter.lower():
            case 'p':
                return 1
            case 'n':
                return 3
            case 'b':
                return 3
            case 'r':
                return 5
            case 'q':
                return 9
            case 'k':
                return 10000