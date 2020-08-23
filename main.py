"""
Main file where the loop of the game is going to be run

Date: 23/08/2020
"""

# Asking
while True:
    try:
        length = int(input("Introduce the number of rows and columns: "))
        break
    except:
        print("That's not a valid option!")

# Creating the board
