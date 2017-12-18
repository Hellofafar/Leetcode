# ------------------------------
# 37. Sudoku Solver
# 
# Description:
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# Empty cells are indicated by the character '.'.
# You may assume that there will be only one unique solution.
# 
# Version: 1.0
# 12/18/17 by Jianfa
# ------------------------------

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        self.solve(board)
        
    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for x in range(1, 10):
                        if self.checkBoard(board, i, j, str(x)):
                            board[i][j] = str(x)
                            
                            if self.solve(board):
                                return True
                            
                            else:
                                board[i][j] = "."
                    
                    return False
                
        return True
    
    def checkBoard(self, board, x, y, item):
        for i in range(9):
            if board[i][y] != "." and board[i][y] == item:
                return False
            if board[x][i] != "." and board[x][i] == item:
                return False
            if board[x / 3 * 3 + i / 3][y / 3 * 3 + i % 3] != "." and board[x / 3 * 3 + i / 3][y / 3 * 3 + i % 3] == item:
                return False
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Backtracking solution.
# Follow the idea of "Straight Forward Java Solution Using Backtracking".
# Try 1 through 9 for each cell. The time complexity should be 9 ^ m (m represents the number of 
# blanks to be filled in), since each blank can have 9 choices.