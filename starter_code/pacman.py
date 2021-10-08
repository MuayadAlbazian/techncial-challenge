"""
Write a module docstring here
"""

__author__ = "Your Name"



def pacman(input_file):
    components = []
    with open(input_file, 'r') as f:
        for i in f.readlines():
            components.append(i.strip('\n').split(' '))
    boardDimensions = components[0]
    initalPosition = components[1]
    movements = components[2]
    walls = components[3:]

    gameBoard = [['O' for x in range(int(boardDimensions[0]))] for y in range(int(boardDimensions[1]))]
    print(gameBoard)

pacman('/Users/muayadalbazian/Documents/pacman/starter_code/input.txt')

""" Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.

Input:
    1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
        (ie. "input.txt")
Outputs:
    1. final_pos_x (int) = final x location of Pacman
    2. final_pos_y (int) = final y location of Pacman
    3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
"""

# return final_pos_x, final_pos_y, coins_collected 
