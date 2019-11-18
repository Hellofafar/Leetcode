# ------------------------------
# 79. Word Search
# 
# Description:
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" 
# cells are those horizontally or vertically neighboring. The same letter cell may not be 
# used more than once.
# 
# Example:
# 
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# Version: 3.0
# 11/17/19 by Jianfa
# ------------------------------

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        
        m = len(board)
        n = len(board[0])
        
        def backtrack(i, j, k):
            # i, j are coordinates of current unit, k is index of the character to check in word
            if k == len(word):
                return True
            
            temp = board[i][j]
            board[i][j] = '#'
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for d in dirs:
                r = i + d[0]
                c = j + d[1]
                if 0 <= r < m and 0 <= c < n and board[r][c] == word[k]:
                    if backtrack(r, c, k+1):
                        return True
            
            board[i][j] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 1):
                        return True
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Improved version of 2.0, use index k to represent the character to check in word,
# saving space during backtrack.
# 
# O(MN * 4MN) time O(4MN) space (4 is four directions)