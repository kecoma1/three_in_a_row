"""
Main file where the loop of the game is going to be run

Date: 23/08/2020
"""
from classes.space import Space
from classes.board import Board


def ask_column():
    """ Method to ask for the column

    :return: void
    """
    global column, inputQuit

    # Asking for the column
    while True:
        try:
            inputQuit = input("\nIntroduce the column (from 0 to length): ")
            column = int(inputQuit)
            if column >= length:
                print("Wrong input. The column must be less than", length)
                continue
            break
        except:
            if inputQuit == 'quit':
                break
            print("Just digits")


def ask_row():
    """Method to ask for the row

    :return: void
    """
    global row, inputQuit

    # Asking for the row
    while True:
        try:
            inputQuit = input("\nIntroduce the row (from 0 to length): ")
            row = int(inputQuit)
            if row >= length:
                print("Wrong input. The row must be less than", length)
                continue
            break
        except:
            if inputQuit == 'quit':
                break
            print("Just digits")


# Asking the user for the input
while True:
    try:
        length = int(input("Introduce the number of rows and columns: "))
        if length < 3:
            print("Input must be bigger than 2")
            continue
        break
    except:
        print("That's not a valid option!")

# Creating the board
game_board = Board(length)

# Variables where we are going to store the play of the user and computer
column = 0
row = 0
inputQuit = ""

# Printing and asking for the play
while True:
    game_board.print_board()

    ask_column()
    if inputQuit == 'quit':
        print("Bye!")
        break

    ask_row()
    if inputQuit == 'quit':
        print("Bye!")
        break

    # Introducing the user's play
    if not game_board.user_input(row, column):
        print("Introduce new values")
        continue

    # Introducing computers random play
    game_board.computer_input()

    # Checking if the user won
    if game_board.did_user_won():
        print("CONGRATULATIONS, YOU WON!")
        game_board.print_board()
        break
    elif game_board.did_computer_won():
        game_board.print_board()
        print("YOU LOST")
        break
