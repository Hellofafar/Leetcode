# ------------------------------
# 79. Word Search
# 
# Description:
# 
# Version: 2.0
# 11/19/18 by Jianfa
# ------------------------------

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, i, j, word):  # Do word search for every unit
                    return True
        
        return False
    
    def backtrack(self, board, i, j, word):
        if len(word) == 0:  # word is found
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        
        temp = board[i][j]
        board[i][j] = '#'
        # Search for four directions
        res = self.backtrack(board, i+1, j, word[1:]) or \
              self.backtrack(board, i, j+1, word[1:]) or \
              self.backtrack(board, i-1, j, word[1:]) or \
              self.backtrack(board, i, j-1, word[1:])
        board[i][j] = temp
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow idea from https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
# In line 37, I used any([self.backtrack(), self.backtrack(), ...]) at first but meet TLE.
# Because with any(), the program will have to execute all four backtrack functions.