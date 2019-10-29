# ------------------------------
# 529. Minesweeper
# 
# Description:
# Let's play the minesweeper game (Wikipedia, online game)!
# 
# You are given a 2D char matrix representing the game board. 'M' represents an unrevealed 
# mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square 
# that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit 
# ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 
# 'X' represents a revealed mine.
# 
# Now given the next click position (row and column indices) among all the unrevealed 
# squares ('M' or 'E'), return the board after revealing this position according to the 
# following rules:
# 
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed 
# blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to 
# a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
# 
# Example 1:
# 
# Input: 
# 
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
# 
# Click : [3,0]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# Note:
# 
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'), which also means the 
# input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been revealed).
# For simplicity, not mentioned rules should be ignored in this problem. For example, you 
# don't need to reveal all the unrevealed mines when the game is over, consider any cases 
# that you will win the game or flag any squares.
# 
# Version: 1.0
# 10/28/19 by Jianfa
# ------------------------------

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        row = click[0]
        col = click[1]
        
        if board[row][col] == "M":
            board[row][col] = "X"
        else:
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # check all squares around board[row][col] to count the number of mines
                    if i == 0 and j == 0:
                        continue
                    r = row + i
                    c = col + j
                    if r < 0 or r >= m or c < 0 or c >= n:
                        continue
                    if board[r][c] == "M" or board[r][c] == "X":
                        if row == 2 and col == 0:
                            print(i, j, r, c, board[r][c])
                        count += 1
            
            if count > 0:
                # an empty square ('E') with at least one adjacent mine is revealed, stop search
                board[row][col] = str(count)
            else:
                # an empty square ('E') with no adjacent mines is revealed, search around
                board[row][col] = "B"            
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # DFS all around squares around board[row][col]
                        if i == 0 and j == 0:
                            continue
                        r = row + i
                        c = col + j
                        if r < 0 or r >= m or c < 0 or c >= n:
                            continue
                        if board[r][c] == "E":
                            self.updateBoard(board, [r, c])
            
        return board

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution from: https://leetcode.com/problems/minesweeper/discuss/99826/Java-Solution-DFS-%2B-BFS
# 1. If click on a mine ('M'), mark it as 'X', stop further search.
# 2. If click on an empty cell ('E'), depends on how many surrounding mine:
#   2.1 Has surrounding mine(s), mark it with number of surrounding mine(s), stop further search.
#   2.2 No surrounding mine, mark it as 'B', continue search its 8 neighbors.
# 
# O(m * n) time, O(1) space