
from player import *
from board import *
import random

print("Hello Everyone, Let's Play Tic Tac Toe!")
print("My name is CPU, and I'll be your opponent. What is your name?")
input_name = input("Input your name >>> ")

player = Player(input_name)
opponent = Player("Computer")
board = Board()
board.print_board()

while board.is_won ==  False:
    print("\n\n")
    print("You play as X, where do you want to put your piece?")
    row = input("Type the row number (0-2)>> ")
    column = input("Type the column number (0-2)>> ")
    row = int(row)
    column = int(column)

    if row >= 0 and row < board.rows and column >= 0 and column < board.columns:
        player_put = board.put_piece("X", row, column)
        print("\nThis is the current board state after your turn: ")
        board.print_board()
        if board.check_win("X"):
            print("{} won!".format(player.name))
    else:
        print("Oops, wrong input position ... lets retry... ")

    computer_put = False
    while player_put and computer_put == False and not board.is_won:
        random_row = random.randint(0, board.rows - 1)
        random_column = random.randint(0, board.columns - 1)
        can_put = board.check_availability(random_row, random_column)
        if can_put:
            computer_put = board.put_piece("O", random_row, random_column)
            print("\nThis is the current board state after computer's turn: ")
            board.print_board()
            if board.check_win("O"):
                print("{} won!".format(opponent.name))

print("Thanks a lot for playing Tic Tac Toe!")