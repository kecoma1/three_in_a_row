'''
File where the board of the game is going to be defined.

Author: Kevin de la Coba Malam
Date: 22/08/2020
'''
from classes import space

# Class that defines a board
class board:

    # Constructor of the board, length refers to 
    # length*length spaces of the board
    def __init__(self, length):
        self.length = length
        self.spaces = space[length][length]


    # Method to print the board
    def print_board(self):
        print("Board of the game.", length, "*", length)
        i = 0
        while i < self.length:
            
            n = 0
            while n < self.length:
                print(self.spaces[i][n].content, end=" ")
                

