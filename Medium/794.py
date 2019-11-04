# ------------------------------
# 794. Valid Tic-Tac-Toe State
# 
# Description:
# A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is 
# possible to reach this board position during the course of a valid tic-tac-toe game.

# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " 
# character represents an empty square.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always places "O" 
# characters.
# "X" and "O" characters are always placed into empty squares, never filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, 
# or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# 
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
# 
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
# 
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
# 
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
# 
# Note:
# board is a length-3 array of strings, where each string board[i] has length 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.
# 
# Version: 1.0
# 11/03/19 by Jianfa
# ------------------------------

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        turns = 0 # use turns += 1 to represent X moved, use turns -= 1 to represent O moved
        xwin = False
        owin = False
        # for row, col, diag, antidiag
        # +1 to represent X, -1 to represent O
        row = [0] * 3
        col = [0] * 3
        diag = 0
        antidiag = 0
        
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    turns += 1
                    row[i] += 1
                    col[j] += 1
                    if i == j:
                        diag += 1
                    if i + j == 2:
                        antidiag += 1
                elif board[i][j] == "O":
                    turns -= 1
                    row[i] -= 1
                    col[j] -= 1
                    if i == j:
                        diag -= 1
                    if i + j == 2:
                        antidiag -= 1
        
        # any line has three 'X', xwin is True
        # any line has three 'O', owin is True
        xwin = 3 in row or 3 in col or diag == 3 or antidiag == 3
        owin = -3 in row or -3 in col or diag == -3 or antidiag == -3
        
        # one player wins but turns doesn't represent it moved correctly
        if xwin and turns != 1 or owin and turns != 0:
            return False
        else:
            return turns == 0 or turns == 1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/valid-tic-tac-toe-state/discuss/117580/Straightforward-Java-solution-with-explaination
# Use some variable to represent numbers of 'X' or 'O' at one line.
# +1 and -1 to represent 'X' and 'O', update the variables corresponding to meeting a 'X' or 'O'