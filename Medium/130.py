# ------------------------------
# 130. Surrounded Regions
# 
# Description:
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Example:
# X X X X
# X O O X
# X X O X
# X O X X
# 
# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
# 
# Version: 1.0
# 08/16/18 by Jianfa
# ------------------------------

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) <= 2 or len(board[0]) <= 2:
            return
        
        def alter(i, j):  # Alter 'O' at the border to 'Y'
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'Y'
                map(alter, (i-1, i+1, i, i), (j, j, j+1, j-1))
        
        for i in range(len(board)):
            alter(i, 0)
            alter(i, len(board[0]) - 1)
                  
        for j in range(len(board[0])):
            alter(0, j)
            alter(len(board)-1, j)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from https://leetcode.com/problems/surrounded-regions/discuss/41612/A-really-simple-and-readable-C++-solutiononly-cost-12ms
# and problem 200.
# The key idea is to alter 'O' at the border and all its adjacent '0' to 'Y' (or some other symbol).
# Then flip all the rest 'O' to 'X', and revert all the 'Y' to 'O'.