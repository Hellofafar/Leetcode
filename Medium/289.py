# ------------------------------
# 289. Game of Life
# 
# Description:
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton 
# devised by the British mathematician John Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts 
# with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the 
# above Wikipedia article):
# 
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
# 
# Version: 1.0
# 11/08/17 by Jianfa
# ------------------------------

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                liveNeighbour = self.countLives(board, i, j, m, n)
                if board[i][j] == 1 and liveNeighbour >=2 and liveNeighbour <= 3:
                    board[i][j] = 3
                
                elif board[i][j] == 0 and liveNeighbour == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] / 2  # if python 3 here is board[i][j] // 2
    
    def countLives(self, board, i, j, m, n):
        lives = 0
        for x in range(max(i-1, 0), min(i+2, m)):  # At first I wrote min(i+1, m-1) which led to a wrong range
            for y in range(max(j-1, 0), min(j+2, n)):
                lives += board[x][y] % 2
        
        lives -= board[i][j] % 2
        return lives

# ------------------------------
# Summary:
# Use 2-digit number to represent state transition:
# 00: 0 -> 0  (0)
# 01: 1 -> 0  (1)
# 10: 0 -> 1  (2)
# 11: 1 -> 1  (3)
# First calculate the number of 1's (or 1 in 1st state, e.g. 01 and 11) around the target position
# Then modify the state in place. For example, 0 to 2 means dead to live, because 00 - > 01
# Finally traverse every cell again, to make the result only 0 or 1.