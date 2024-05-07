from board import Board
from player import Player
from randomBot import RandomBot;
from minimaxBot import MinimaxBot
from time import sleep
import chess
import os
from evaluate import evaluate

def main():
    bot1 = RandomBot()
    #Minimax bot must be black
    bot2 = MinimaxBot(3)
    
    #simulate(bot1, bot2, 1)
    playerVsBot(bot2)
    #playerVsPlayer()

def playerVsBot(bot):
    player = Player("Player")
    board = Board()
    turn = True

    while not board.outcome():
        printBoard(board, player, bot)

        if turn:
            print("Player Turn")
            player.move(board)
        else:
            bot.move(board)
            sleep(1)
        
        turn = not turn

    
    printBoard(board, player, bot) 

    outcome = board.outcome()

    if outcome.winner == chess.WHITE:
        print("You win.")
    elif outcome.winner == chess.BLACK:
        print("Bot wins.")
    else:
        print("Draw.")


def playerVsPlayer():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    board = Board()
    turn = True

    while not board.outcome():
        printBoard(board, player1, player2)

        if turn:
            print("Player 1 Turn")
            player1.move(board)
        else:
            print("Player 2 Turn")
            player2.move(board)
        
        turn = not turn

    printBoard(board, player1, player2) 

    outcome = board.outcome()

    if outcome.winner == chess.WHITE:
        print("You win.")
    elif outcome.winner == chess.BLACK:
        print("Bot wins.")
    else:
        print("Draw.")

def simulate(white, black, games):

    draws = 0
    wWins = 0
    bWins = 0

    # Set colors of bots to be able to evaluate the board

    for _ in range(games):
        outcome = playGame(white, black)

        if outcome.winner == chess.WHITE:
            print("White wins.")
            wWins += 1
        elif outcome.winner == chess.BLACK:
            print("Black wins.")
            bWins += 1
        else:
            print("Draw.")
            draws += 1
        sleep(4)
        
    print("Simulated: " + str(games) + " | White: " + str(wWins) + " | Black: " + str(bWins) + " | Draws: " + str(draws))

def playGame(white, black):

    board = Board()
    turn = True
    
    while not board.outcome():
        printBoard(board, white, black)
        
        if board.isDraw():
            break

        if turn:
            white.move(board)
        else:
            black.move(board)

        turn = not turn
        
        sleep(0.2)

        outcome = board.outcome()

    printBoard(board, white, black)
    return outcome


def printBoard(board, white, black):
    evalW = evaluate(board)
    evalB = -1 * evalW
    boardP = board.toString()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Black: {black.name()}, Eval: {evalB}\n" + "---------------\n" + boardP + "\n---------------" + f"\nWhite: {white.name()}, Eval: {evalW}")


if __name__ == "__main__":
    main()