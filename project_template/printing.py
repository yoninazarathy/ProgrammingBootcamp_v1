#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:42:35 2023

@author: uqjnazar
"""

def print_board(board):
    print("  ", end= "")
    for i in range(len(board)):
        print(i+1, end = " ")
    print()
    for i in range(len(board)):
        print(i+1, end = " ")
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()