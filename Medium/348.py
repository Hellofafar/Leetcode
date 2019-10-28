# ------------------------------
# 348. Design Tic-Tac-Toe
# 
# Description:
# Design a Tic-tac-toe game that is played between two players on a n x n grid.
# 
# You may assume the following rules:
# 
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal 
# row wins the game.
# 
# Example:
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
# 
# TicTacToe toe = new TicTacToe(3);
# 
# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
# 
# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
# 
# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
# 
# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
# 
# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
# 
# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
# 
# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
# 
# Follow up:
# Could you do better than O(n2) per move() operation?
# 
# Version: 1.0
# 10/27/19 by Jianfa
# ------------------------------

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        toAdd = 1 if player == 1 else -1
        self.rows[row] += toAdd
        self.cols[col] += toAdd
        
        size = len(self.rows)
        if row == col:
            self.diagonal += toAdd
        if row == size - 1 - col:
            self.anti_diagonal += toAdd
        
        if abs(self.rows[row]) == size or abs(self.cols[col]) == size or abs(self.diagonal) == size or abs(self.anti_diagonal) == size:
            return player
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Smart solution from: https://leetcode.com/problems/design-tic-tac-toe/discuss/81898/Java-O(1)-solution-easy-to-understand
# Idea is to keep a count for the row, column, diagonal or anti-diagonal to check if the count
# is equal to the n at some point.
# If so, then some one wins.
# 
# O(1) times, O(n) space