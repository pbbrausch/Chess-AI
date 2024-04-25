from board import Board
from bot import Bot;
from time import sleep
import chess
import os

def main():
    board = Board()
    bot1 = Bot()
    bot2 = Bot()
    games = 100

    simulate(bot1, bot2, board, games)

def simulate(bot1, bot2, board, games):

    draws = 0
    white = 0
    black = 0

    for _ in range(games):
        while not board.isDraw():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---------------\n" + board.toString() + "\n---------------")
            if not bot1.makeMove(board):
                break
            if not bot2.makeMove(board):
                break
            #sleep(1.5)

        outcome = board.outcome()

        if outcome:
            if outcome.winner == chess.WHITE:
                white += 1
            elif outcome.winner == chess.BLACK:
                black += 1
            else:
                draws += 1

        board.reset()
        
    print("Simulated: " + str(games) + " | White: " + str(white) + " | Black: " + str(black) + " | Draws: " + str(draws))

    

if __name__ == "__main__":
    main()