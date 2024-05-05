from board import Board
from randomBot import RandomBot;
from minimaxBot import MinimaxBot
from time import sleep
import chess
import os
from random import choice
from evaluate import evaluate

def main():
    bot1 = MinimaxBot(2)
    bot2 = MinimaxBot(2)
    
    simulate(bot1, bot2, 1)

def simulate(bot1, bot2, games):

    board = Board()

    draws = 0
    white = 0
    black = 0

    turn = choice((True, False))
    startTurn = turn

    # Set colors of bots to be able to evaluate the board
    if (turn):
        bot1.setColor(chess.WHITE)
        bot2.setColor(chess.BLACK)
    else:
        bot1.setColor(chess.BLACK)
        bot2.setColor(chess.WHITE)

    for _ in range(games):
        while True:
            evalB = evaluate(board, chess.BLACK)
            evalW = evaluate(board, chess.WHITE)
            boardP = board.toString()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Black: {bot1.name() if startTurn == False else bot2.name()}, Eval: {evalB}\n" + "---------------\n" + boardP + "\n---------------" + f"\nWhite: {bot2.name() if startTurn == False else bot1.name()}, Eval: {evalW}")

            if board.isDraw():
                break

            if (turn):
                bot1.makeMove(board)
            else:
                bot2.makeMove(board)

            turn = not turn
            sleep(1)

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