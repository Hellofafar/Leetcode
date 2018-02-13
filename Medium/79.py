# ------------------------------
# 79. Word Search
# 
# Description:
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells 
# are those horizontally or vertically neighboring. The same letter cell may not be used more 
# than once.
# 
# For example,
# Given board =
# 
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# 
# Version: 1.0
# 01/21/18 by Jianfa
# ------------------------------

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False
        
        first = word[0]
        starts = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for idx, x in enumerate(board[i]):
                if x == first:
                    starts.append((i, idx))
        
        checked = []
        for pos in starts:
            x = pos[0]
            y = pos[1]
            if self.backtrack(board, word, x, y, checked):
                return True
        
        return False
            
            
    def backtrack(self, board, word, i, j, checked):
        if not word:
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if (i, j) in checked:
            return False
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if board[i][j] == word[0]:
            checked.append((i,j))
            for d in dirs:
                new_i = i + d[0]
                new_j = j + d[1]
                if self.backtrack(board, word[1:], i+d[0], j+d[1], checked):
                    return True
            checked.pop()
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()
    board = [["A"]]
    word = "A"
    test.exist(board, word)

# ------------------------------
# Summary:
# Backtrack solution. The special point is, as long as one possible path is found, return true.