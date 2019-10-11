# ------------------------------
# 419. Battleships in a Board
# 
# Description:
# Given an 2D board, count how many battleships are in it. The battleships are represented 
# with 'X's, empty slots are represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only 
# be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of 
# any size.
# At least one horizontal or vertical cell separates between two battleships - there are 
# no adjacent battleships.
# 
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# 
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a 
# cell separating between them.
# 
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value 
# of the board?
# 
# Version: 1.0
# 10/10/19 by Jianfa
# ------------------------------

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        n = len(board)
        m = len(board[0])
        count = 0
        
        for i in range(n):
            for j in range(m):
                # Find the first cell of each battleship
                if board[i][j] == ".":
                    continue
                if i > 0 and board[i-1][j] == "X":
                    continue
                if j > 0 and board[i][j-1] == "X":
                    continue
                count += 1
        
        return count

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/battleships-in-a-board/discuss/90902/Simple-Java-Solution
# Going over all cells, we can count only those that are the "first" cell of the battleship. 
# First cell will be defined as the most top-left cell. We can check for first cells by only 
# counting cells that do not have an 'X' to the left and do not have an 'X' above them.

