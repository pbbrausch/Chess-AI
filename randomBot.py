from random import choice

class RandomBot(): 
    def setColor(self, color):
        self.color = color   

    def makeMove(self, board):
        board.makeMove(choice(board.getLegalMoves()))

    def name(self):
        return "Random Bot"