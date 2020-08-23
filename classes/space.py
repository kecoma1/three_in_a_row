"""
File where the spaces of the game are going to be defined

Author: Kevin de la Coba Malam
Date: 22/08/2020

Date: 23/08/2020
    Modified the attributes of the class, I removed the boolean attribute
    occupied, there's no need to use it.
    Also changed the style of the documentation
    Added method reset_space
"""


class Space:
    """ Class that defines the space. Empty = '*', User = 'X', Computer = '0' """

    def __init__(self):
        """ Constructor of the class space """
        self.content = '*'

    def user_occupies(self):
        """ Method to set the space to be occupied by the user

        :return: void
        """
        self.content = 'X'

    def computer_occupies(self):
        """  Method to set the space to be occupied by the computer

        :return: void
        """
        self.content = '0'

    def reset_space(self):
        """ Method to reset the space

        :return: void
        """
        self.content = '*'