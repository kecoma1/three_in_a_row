"""
File where the board of the game is going to be defined.

Author: Kevin de la Coba Malam
Date: 22/08/2020

Date: 23/08/2020
    Added methods to see who won, this methods call other methods which
    check the rows, columns and also the diagonal of the game.
    The cost of the algorithms to check the rows, columns and horizontal is O(n)
    but the cost for checking the entire field before calling the these methods
    is O(n²).
    Changed the style of the documentation

Date: 25/08/2020
    Minor change in method print_board
"""
from classes import space
import random


class Board:
    """ Class that defines a board """

    def __init__(self, length):
        """ Constructor of the board, length refers to length*length spaces of the board

        :param length: (int) length of the board, also the height
        """
        self.length = length
        self.spaces = [[space.Space() for i in range(length)] for j in range(length)]

    def print_board(self):
        """ Method to print the board

        :return: void
        """
        print("\nBoard of the game. ", self.length, "*", self.length, "\n")
        i = 0
        print(end="  ")
        while i < self.length:
            print(" ", i, end=" ")
            i += 1

        i = 0
        print("")
        while i < self.length:
            n = 0
            print(i, end=" ")
            while n < self.length:
                # Printing every space
                print(" ", self.spaces[i][n].content, end=" ")
                n += 1
            print("")
            i += 1

    def did_computer_won(self):
        """ Method to check if the computer won

        :return: Boolean value
            True if the computer won,
            False if not
        """
        # Looking for a '0'
        i = 0
        while i < self.length:
            n = 0
            while n < self.length:
                # We found the computer char
                if self.spaces[i][n].content == '0':
                    if self.check_vertical(n, '0') or self.check_horizontal(i, '0') or self.check_diagonal('0'):
                        return True
                n += 1
            i += 1
        return False

    def did_user_won(self):
        """ Method to check if the user won

        :return: Boolean value
            True if the user won,
            False if not
        """
        # Looking for a 'X'
        i = 0
        while i < self.length:
            n = 0
            while n < self.length:
                # We found the user char
                if self.spaces[i][n].content == 'X':
                    if self.check_vertical(n, 'X') or self.check_horizontal(i, 'X') or self.check_diagonal('X'):
                        return True
                n += 1
            i += 1
        return False

    def check_vertical(self, v, player):
        """ Method to check a row to see if the player has won

        :param v: (int) Column to check
        :param player: (char) Player to check
        :return: Boolean value
            True if the column has just that char,
            False if not
        """
        i = 0
        while i < self.length:
            if self.spaces[i][v].content != player:
                return False
            i += 1
        return True

    def check_horizontal(self, h, player):
        """ Method to check a column to see if the player has won

        :param h: (int) Row to check
        :param player: (char) Player to check
        :return: Boolean value
            True if the row has just that char,
            False if not
        """
        i = 0
        while i < self.length:
            if self.spaces[h][i].content != player:
                return False
            i += 1
        return True

    def check_diagonal(self, player):
        """ Method to check the diagonal with a space to see if the player has won

        :param player: (char) Player to check
        :return: Boolean value
            True if the diagonal has just that char,
            False if not
        """
        if self.check_first_diagonal(player) or self.check_second_diagonal(player):
            return True

    def check_first_diagonal(self, player):
        """ Method to check first diagonal \

        :param player: Player to check
        :return: Boolean value
            True if the first diagonal is full
            False if not
        """
        i = 0
        n = 0
        # Checking the first diagonal \
        while i < self.length:
            if self.spaces[i][n].content != player:
                return False
            i += 1
            n += 1
        return True

    def check_second_diagonal(self, player):
        """ Method to check the second diagonal /

        :param player: Player to check
        :return: Boolean value
            True if the first diagonal is full
            False if not
        """
        i = 0
        n = self.length - 1
        # Checking the second diagonal /
        while i < self.length:
            if self.spaces[i][n].content != player:
                return False
            i += 1
            n -= 1
        return True

    def user_input(self, row, column):
        """ Method to introduce the user input

        :param column: Column which the user chose
        :param row: Row which the user chose
        :return: Boolean
            True if it is possible to occupy this place
            False if not
        """
        if self.check_entire_board():
            self.reset_board()

        if self.spaces[row][column].content == '*':
            self.spaces[row][column].user_occupies()
            return True
        else:
            print("Space occupied")
            return False

    def computer_input(self):
        """ Method to introduce a random computer input

        :return: void
        """
        if self.check_entire_board():
            self.reset_board()
        row = 0
        column = 0
        while True:
            row = random.randrange(0, self.length)
            column = random.randrange(0, self.length)
            if self.spaces[row][column].content == '*':
                self.spaces[row][column].computer_occupies()
                break

    def check_entire_board(self):
        """ Method to check if the entire field is occupied

        :return: Boolean value
            True if the entire field is occupied,
            False if not
        """
        i = 0
        while i < self.length:
            n = 0
            while n < self.length:
                if self.spaces[i][n].content == '*':
                    return False
                n += 1
            i += 1
        return True

    def reset_board(self):
        """ Method to reset the entire board

        :return: void
        """
        self.print_board()
        print("\n Full board, reseting it")

        i = 0
        while i < self.length:
            n = 0
            while n < self.length:
                self.spaces[i][n].reset_space()
                n += 1
            i += 1
