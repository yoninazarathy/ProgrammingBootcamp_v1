#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:38:51 2023

@author: uqjnazar
"""

from defs import *
from printing import *

def init_board():
    return [["_" for _ in range(board_dim)] for _ in range(board_dim)]

def is_piece(c):
    return c == 'X' or c == 'O'

def check_victory(board):
    #Returns 'X', 'O', "StaleMate", or None depending on victory or not
    
    #check diagonal
    p = board[0][0]
    if is_piece(p):
        win = True
        for i in range(board_dim):
            if board[i][i] != p:
                win = False
                break
        if win:
            return p

    #check anti-diagonal
    p = board[0][-1]
    if is_piece(p):    
        win = True
        for i in range(board_dim):
            if board[i][board_dim-1-i] != p:
                win = False
                break
        if win:
            return p

    #check rows
    for i in range(board_dim):
        p = board[i][0]
        if is_piece(p):    
            win = True
            for j in range(board_dim):
                if board[i][j] != p:
                    win = False
                    break
            if win:
                return p

    #check columns
    for j in range(board_dim):
        p = board[0][j]
        if is_piece(p):    
            win = True
            for i in range(board_dim):
                if board[i][j] != p:
                    win = False
                    break
            if win:
                return p
        
    #if here then no victory, just check if any empty spot then return None
    for i in range(board_dim):
        for j in range(board_dim):
            if board[i][j] == "_":
                return None
    
    #If here then no victory and no empty spot
    return "StaleMate"
    

def main():
    print("Welcome to Tic Tac Toe!\n")
    player_turn = "X"
    board = init_board()

    #Game loop
    while True:
        print()
        print_board(board)
        print(f"\nIt is turn for player {player_turn}")
        print(f"Row 1--{board_dim}: ", end = '')
        row = int(input())
        print(f"Col 1--{board_dim}: ", end = '')
        col = int(input())
        row = row - 1
        col = col - 1
        if board[row][col] != "_":
            print("That spot is taken try again.")
        else:
            board[row][col] = player_turn
            if player_turn == "X":
                player_turn = "O"
            else:
                player_turn = "X"
                
        victory = check_victory(board)
        if victory == "StaleMate":
            print("No one wins!")
            break
        elif victory in ["X", "O"]:
            print(f"Player {victory} wins!")
            break

if __name__ == "__main__":
    main()