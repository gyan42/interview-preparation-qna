"""
https://leetcode.com/problems/game-of-life/

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

"""
from typing import List

"""
------------|----------|------------
|(i-1, j-1) | (i-1, j) | (i-1, j+1)|
------------|----------|------------
|(i,   j-1) | (i,   j) | (i,   j+1)|
------------|----------|------------
|(i+1, j-1) | (i+1, j) | (i+1, j+1)|
------------|----------|------------
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rl, cl = len(board), len(board[0])
        for i in range(rl):
            for j in range(cl):
                live_nei = 0

                for r, c in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1), (i, j-1)]:
                    if 0 <= r < rl and 0 <= c < cl and abs(board[r][c]) == 1:
                        live_nei += 1

                # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                # Any live cell with more than three live neighbors dies, as if by over-population.
                if board[i][j] == 1 and (live_nei < 2 or live_nei > 3):
                    board[i][j] = -1  # Temp state

                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                if board[i][j] == 0 and live_nei == 3:
                    board[i][j] = 2

        # Any live cell with two or three live neighbors lives on to the next generation.
        for i in range(rl):
            for j in range(cl):
                board[i][j] = 1 if board[i][j] > 0 else 0