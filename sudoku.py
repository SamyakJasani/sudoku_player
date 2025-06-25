# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:56:09 2023

@author: samyak
"""

import sys


def quit():
    sys.exit()
    
    
def printBoard(board):
    print("\n")
    print("               |           |")
    print("   -------------------------------------")
    print("   |", board[1], "|", board[2], "|", board[3], "|", board[4], "|", board[5], "|", board[6], "|", board[7], "|", board[8], "|", board[9], "|")
    print("   -------------------------------------")
    print("   |", board[10], "|", board[11], "|", board[12], "|", board[13], "|", board[14], "|", board[15], "|", board[16], "|", board[17], "|", board[18], "|")  
    print("   -------------------------------------")
    print("   |", board[19], "|", board[20], "|", board[21], "|", board[22], "|", board[23], "|", board[24], "|", board[25], "|", board[26], "|", board[27], "|")
    print("-------------------------------------------")
    print("   |", board[28], "|", board[29], "|", board[30], "|", board[31], "|", board[32], "|", board[33], "|", board[34], "|", board[35], "|", board[36], "|")
    print("   -------------------------------------")
    print("   |", board[37], "|", board[38], "|", board[39], "|", board[40], "|", board[41], "|", board[42], "|", board[43], "|", board[44], "|", board[45], "|")
    print("   -------------------------------------")
    print("   |", board[46], "|", board[47], "|", board[48], "|", board[49], "|", board[50], "|", board[51], "|", board[52], "|", board[53], "|", board[54], "|")
    print("-------------------------------------------")
    print("   |", board[55], "|", board[56], "|", board[57], "|", board[58], "|", board[59], "|", board[60], "|", board[61], "|", board[62], "|", board[63], "|")
    print("   -------------------------------------")
    print("   |", board[64], "|", board[65], "|", board[66], "|", board[67], "|", board[68], "|", board[69], "|", board[70], "|", board[71], "|", board[72], "|")
    print("   -------------------------------------")
    print("   |", board[73], "|", board[74], "|", board[75], "|", board[76], "|", board[77], "|", board[78], "|", board[79], "|", board[80], "|", board[81], "|")
    print("-------------------------------------------")
    print("               |           |")
    
    
def unchangeable(position):
    return position in given
        

def notInSquare(number, position):
    for s in squares:
        if position in s:
            for pos in s:
                if board[pos] == number:
                    return False 
            return True 


def notInColumn(number, position):
    for col in cols:
        if position in col:
            for pos in col:
                if board[pos] == number:
                    return False 
            return True


def notInRow(number, position):
    for row in rows:
        if position in row:
            for pos in row:
                if board[pos] == number:
                    return False 
            return True


def makeMove(number, position):
    if not unchangeable(position):
        if notInSquare(number, position) and notInRow(number, position) and notInColumn(number, position):
            board[position] = number
            printBoard(board)
            if ' ' not in board.values():
                print("Success! You solved the sudoku puzzle")
                quit()
        else:
            print("\nIllegal move! You can't do that")
            
    else:
        print(f"\nPosition {position} is unchangeable!")
    play()
    
def play():
    try: 
        number = int(input("Enter the number you want to play (any other key to exit the game): "))
    except:
        quit()
    if number > 9:
        print("\nNumber should be less than 10")
        play()
    position = int(input(f"Enter the position you want to occupy for {number}: "))
    makeMove(number, position)
    return 


board = {1: ' ', 2: 7, 3: ' ', 4: 5, 
         5: 8, 6: 3, 7: ' ',  8: 2, 
         9: ' ', 10: ' ', 11: 5, 12: 9,
        13: 2, 14: ' ', 15: ' ', 16: 3,
        17: ' ', 18: ' ', 19: 3, 20: 4,
        21: ' ', 22: ' ', 23: ' ', 24: 6,
        25: 5, 26: ' ', 27: 7, 28: 7,
        29: 9, 30: 5, 31: ' ', 32: ' ',
        33: ' ', 34: 6, 35: 3, 36: 2,
        37: ' ', 38: ' ', 39: 3, 40: 6,
        41: 9, 42: 7, 43: 1, 44: ' ',
        45: ' ', 46: 6, 47: 8, 48: ' ',
        49: ' ', 50: ' ', 51: 2, 52: 7,
        53: ' ', 54: ' ', 55: 9, 56: 1,
        57: 4, 58: 8, 59: 3, 60: 5,
        61: ' ', 62: 7, 63: 6, 64: ' ',
        65: 3, 66: ' ', 67: 7, 68: ' ',
        69: 1, 70: 4, 71: 9, 72: 5,
        73: 5, 74: 6, 75: 7, 76: 4,
        77: 2, 78: 9, 79: ' ', 80: 1,
        81: 3}

s1 = {1, 2, 3, 10, 11, 12, 19, 20, 21}
s2 = {4, 5, 6, 13, 14, 15, 22, 23, 24}
s3 = {7, 8, 9, 16, 17, 18, 25, 26, 27}
s4 = {28, 29, 30, 37, 38, 39, 46, 47, 48}
s5 = {31, 32, 33, 40, 41, 42, 49, 50 ,51}
s6 = {34, 35, 36, 43, 44, 45, 52, 53, 54}
s7 = {55, 56, 57, 64, 65, 66, 73, 74, 75}
s8 = {58, 59, 60, 67, 68, 69, 76, 77, 78}
s9 = {61, 62, 63, 70, 71, 72, 79, 80, 81}
squares = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

row1 = set(range(1, 10))
row2 = set(range(10, 19))
row3 = set(range(19, 28))
row4 = set(range(28, 37))
row5 = set(range(37, 46))
row6 = set(range(46, 55))
row7 = set(range(55, 64))
row8 = set(range(64, 73))
row9 = set(range(73, 82))
rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]


col1 = {1, 10, 19, 28, 37, 46, 55, 64, 73}
col2 = {2, 11, 20, 29, 38, 47, 56, 65, 74}
col3 = {3, 12, 21, 30, 39, 48, 57, 66, 75}
col4 = {4, 13, 22, 31, 40, 49, 58, 67, 76}
col5 = {5, 14, 23, 32, 41, 50, 59, 68, 77}
col6 = {6, 15, 24, 33, 42, 51, 60, 69, 78}
col7 = {7, 16, 25, 34, 43, 52, 61, 70, 79}
col8 = {8, 17, 26, 35, 44, 53, 62, 71, 80}
col9 = {9, 18, 27, 36, 45, 54, 63, 72, 81}
cols = [col1, col2, col3, col4, col5, col6, col7, col8, col9]


given = set()
for pos in board:
    if board[pos] != ' ':
        given.add(pos)
print("\n\nWelcome to 9x9 Sudoku")
print("\nPositions are numbered 1–81, row-wise left to right, top to bottom.")
printBoard(board)
play()