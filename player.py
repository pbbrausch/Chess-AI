import chess

class Player(): 
    def __init__(self, name):
        self.playerName = name

    def move(self, board):
        while True:
            try:
                move = chess.Move.from_uci(str(input("Make a move: ")))
                if board.makeMove(move):
                    return
            except:
                moves = str(board.getLegalMoves()).replace("Move.from_uci(",'').replace(")",'').replace("'",'')
                print(f"Wrong format, try: {moves}")
                pass
            
    def name(self):
        return self.playerName