"""
    Author: Simon Zhang

    Date: Jan 25, 2021

    Description: An implementation of the game 'Connect Four' in Python. It imports the random module.
"""

import random

def display_board(rows, columns, board):
    """This function accepts the rows, columns and the connect four board as parameters. It will print
    a connect four grid board using characters, including the positions of the "X" and "O" spaces. It numbers
    the columns at the top of the grid. This function does not return anything. """

    # number the columns
    for x in range(columns):
        print(" ", x+1, "", end = "")
    print()
    print("+---"* columns + "+")

    # print the tiles, go in reverse so that the counters are filling up from the bottom
    for column in range(rows-1, -1, -1):
          print("| ",end = "")
          print(" | ".join(board[column]), end="")
          print(" |")
          print("+---"* columns, end = "")
          print("+")

def decide_first_move():
    """This function accepts no parameters. It prompts the user for if they want to make the first move and returns True
    if they do, and returns False if they don't. """

    while True:
        print("\nWould you like to make the first move? (Y/N)")
        user_input = input().upper()
        if user_input == "Y":
            return True
        elif user_input == "N":
            return False
        else:
            print("That is not a valid input. Please enter 'y', 'Y', 'n', or 'N'")

def make_user_move(rows, columns, board):
    """This function accepts the rows, columns, and connect four board as parameters. It prompts the user for
    the column they want to make a move on, and places an "X" on the lowest available space in the column on the board.
    It checks if the column is filled or not, and if the column is in the range of columns on the board. This function does
    not return anything. """

    valid_move = False
    while True:
        try:
            column = int(input("What column would you like to make a move on? \n")) - 1
            # check if the user entered a number within the range of columns
            if 0 <= column <= columns - 1:
                # loop through the list and look for the first position of a blank space in that column
                for row in range(len(board)):
                    if board[row][column] == " ":
                        board[row][column] = "X"
                        valid_move = True
                        break
                # if we went through the whole list and found no blank spaces
                if not valid_move:
                    print("That column is filled up!")
                # the move as valid, break out of the main user input validation loop
                else:
                    break
            # if the user did not enter a number within the range of columns
            else:
                print("That is not a valid column!")
        # if the user did not enter an integer
        except ValueError:
            print("Please enter an integer between 1-" + str(columns) + "!")

def make_computer_move(rows, columns, board):
    """This function accepts the rows, columns, and connect four board as parameters. It will randomly select a
    column to make a move on (placing an "O" in the lowest available space in the column on the board)
    between the range of columns. If the column is already filled up, it will choose another column. It also prints
    which column it has made a move on. This function returns nothing. """

    valid_move = False
    while True:
        # generate a random column
        column = random.randint(0, columns-1)

        # find the lowest space in the column
        for row in range(len(board)):
            # if a space has been found
            if board[row][column] == " ":
                board[row][column] = "O"
                valid_move = True
                break
        if valid_move:
            break
    print("The computer moved on column", str(column+1)+ ".")

def winner(rows, columns, board):
    """ This function accepts the rows, columns and the connect four board as parameters. If there are no winners, it
    will return nothing. If the user has won, it will return "X", if the computer has won, it will return "O". """
    # Check rows for winner
    for row in board:
        for x in range(3, len(row)):
            if row[x-3] == row[x-2] == row[x-1] == row[x] and row[x] != " ":
                return row[x]

    # Check columns for winner:
    for column in range(columns):
        for row in range(3, len(board)):
            if board[row-3][column] == board[row-2][column] == board[row-1][column] == board[row][column] and board[row][column] != " ":
                return board[row][column]

    # find bottom left to top right diagonals
    right_diagonals = []

    # right diagonals created by starting on the left side
    for x in range(0, rows-3):
        diagonal = []
        row = x
        column = 0
        # hitting the edge of the board
        while column != columns and row != rows:
            diagonal.append(board[row][column])
            row += 1
            column += 1
        right_diagonals.append(diagonal)

    # right diagonals created by starting on the bottom side
    for x in range(1, columns-3):
        diagonal = []
        column = x
        row = 0
        # hitting the edge of the board
        while column != columns and row != rows:
            diagonal.append(board[row][column])
            row += 1
            column += 1
        right_diagonals.append(diagonal)

    # checking right diagonals for four in a row
    for diagonal in right_diagonals:
        for x in range(len(diagonal)):
             if diagonal[x-3] == diagonal[x-2] == diagonal[x-1] == diagonal[x] and diagonal[x] != " ":
                return diagonal[x]

    # find bottom right to top left diagonals
    left_diagonals = []

    # left diagonals created by starting on the right side
    for x in range(0, rows-3):
        diagonal = []
        row = x
        column = columns - 1
        # hitting the edge of the board
        while column != -1 and row != rows:
            diagonal.append(board[row][column])
            row += 1
            column -=1
        left_diagonals.append(diagonal)

    # left diagonals created by starting on the bottom
    for x in range(3, columns-1):
        diagonal = []
        row = 0
        column = x
        # hitting the edge of the board
        while column != -1 and row != rows:
            diagonal.append(board[row][column])
            row += 1
            column -= 1
        left_diagonals.append(diagonal)

    # checking left diagonals for four in a row
    for diagonal in left_diagonals:
        for x in range(len(diagonal)):
             if diagonal[x-3] == diagonal[x-2] == diagonal[x-1] == diagonal[x] and diagonal[x] != " ":
                return diagonal[x]

def choose_board():
    """This function accepts no parameters. It prints out a list of available board sizes and prompts the user to select
    a board. It returns a list with the row and column of the board selected by the user."""

    boards = [[5, 6], [5, 7], [5, 8], [6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8]]
    
    print("Which board size would you like to play?")
    print("""
1. 5x6
2. 5x7
3. 5x8
4. 6x6
5. 6x7
6. 6x8
7. 7x6
8. 7x7
9. 7x8
""")
    while True:
        try:
            user_choice = int(input())
            if 1 <= user_choice <= 9:
                break
            else:
                print("Please enter a number from 1-9!")
        except:
            print("Please enter a number from 1-9!")
    return boards[user_choice-1]

def main():
    """This function defines the mainline logic. It displays the past winners, creates the connect four board
    and allows the user to play connect four against the computer. If the user wins, it adds their name to the
    list of winners. """

    # Display the Hall of Fame
    print("--------------\n HALL OF FAME \n--------------")
    try:
        winners_file = open("HallOfFame.txt", 'r')
        file_line = 1
        for line in winners_file:
            print(file_line, line)
            file_line += 1
        winners_file.close()
    except FileNotFoundError:
        print("No Human Has Ever Beat Me.. mwah-ha-ha-ha!")

    # creating the connect four board
    choosen_board = choose_board()
    rows = choosen_board[0]
    columns = choosen_board[1]
    free_cells = rows * columns

    cnt_four_board = []
    for x in range(rows):
        cnt_four_board.append([' '] * columns)

    # decide if the user goes first
    users_turn = decide_first_move()

    # while there is no winner and there are free cells, alternate user and computer turns
    while not winner(rows, columns, cnt_four_board) and (free_cells > 0):
        display_board(rows, columns, cnt_four_board)

        if users_turn:
            make_user_move(rows, columns, cnt_four_board)
            users_turn = False

        else:
            make_computer_move(rows, columns, cnt_four_board)
            users_turn = True
        free_cells -= 1

    display_board(rows, columns, cnt_four_board)

    # the user wins
    if (winner(rows, columns, cnt_four_board) == 'X'):
        print("YOU WON!")

        # ask the user for their name and it to the HallOfFame.txt
        name = input("What is your name?\n")
        print("Your name has been added to the Hall of Fame!")
        winners_file = open("HallOfFame.txt", 'a')
        winners_file.write(name + "\n")
        winners_file.close()

    # the computer wins
    elif (winner(rows, columns, cnt_four_board) == 'O'):
        print("THE COMPUTER WON!")

    else:
        print("TIE!")

    print("\n*** GAME OVER ***\n")

main()
