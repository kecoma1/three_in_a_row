''''
File where the spaces of the game are going to be defined

Author: Kevin de la Coba Malam
Date: 22/08/2020
'''

# Class that defines the space. Empty = '*', User = 'X', Computer = '0'
class space:

    # Constructor of the class space
    def __init__(self):
        self.occupied = False
        self.content = '*'

    
    # Method to set the space to be occupied by the user
    def user_occupies(self):
        self.occupied = True
        self.content = 'X'


    # Method to set the space to be occupied by the computer
    def computer_occupies(self):
        self.occupied = True
        self.content = '0'

    
