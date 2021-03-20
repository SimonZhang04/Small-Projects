"""
    Author: Simon Zhang

    Date: Jan 16, 2021

    Description: An implementation of the game Tic-Tac-Toe in Python,
    using a nested list, and everything else we've learned this quadmester!
"""

import random

def winner(board):

    """This function accepts the Tic-Tac-Toe board as a parameter.
    If there is no winner, the function will return the empty string "".
    If the user has won, it will return 'X', and if the computer has
    won it will return 'O'."""
    # Check rows for winner
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != " "):
            return board[row][0]

    # COMPLETE THE REST OF THE FUNCTION CODE BELOW
    # Check columns for winner
    for column in range(3):
        if (board[0][column] == board[1][column] == board[2][column]) and (board[0][column] != " "):
            return board[0][column]

    # Check diagonal (top-left to bottom-right) for winner
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != " "):
        return board[0][0]

    # Check diagonal (bottom-left to top-right) for winner
    if (board[2][0] == board[1][1] == board[0][2]) and (board[2][0] != " "):
        return board[2][0]

    # No winner: return the empty string
    return ""

def display_board(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will print the Tic-Tac-Toe board grid (using ASCII characters)
    and show the positions of any X's and O's.  It also displays
    the column and row numbers on top and beside the board to help
    the user figure out the coordinates of their next move.
    This function does not return anything."""

    print("   1   2   3")
    print("1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("  ---+---+---")
    print("2: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  ---+---+---")
    print("3: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print()

def make_user_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will ask the user for a row and column.  If the row and
    column are each within the range of 0 and 2, and that square
    is not already occupied, then it will place an 'X' in that square."""

    try:
        valid_move = False
        while not valid_move:
            row = int(input("What row would you like to move to (1-3):"))-1
            col = int(input("What col would you like to move to (1-3):"))-1
            if (0 <= row <= 2) and (0 <= col <= 2) and (board[row][col] == " "):
                board[row][col] = 'X'
                valid_move = True
            else:
                print("Sorry, invalid square. Please try again!\n")
    except ValueError:
        print("Please enter integers from 1-3!")


def make_computer_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will randomly pick row and column values between 0 and 2.
    If that square is not already occupied it will place an 'O'
    in that square.  Otherwise, another random row and column
    will be generated."""

    while True:
        random_row = random.randint(0, 2)
        random_column = random.randint(0, 2)
        if board[random_row][random_column] == " ":
            board[random_row][random_column] = "O"
            break
    return board
    # COMPLETE THE REST OF THE FUNCTION CODE BELOW


def main():
    """Our Main Game Loop:"""

    free_cells = 9
    users_turn = True
    ttt_board = [ [ " ", " ", " " ], [ " ", " ", " " ], [ " ", " ", " " ] ]

    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1

    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print("Y O U   W O N !")
    elif (winner(ttt_board) == 'O'):
        print("I   W O N !")
    else:
        print("S T A L E M A T E !")
    print("\n*** GAME OVER ***\n")

# Start the game!
main()