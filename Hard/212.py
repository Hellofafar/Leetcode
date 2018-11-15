# ------------------------------
# 212. Word Search II
# 
# Description:
# Given a 2D board and a list of words from the dictionary, find all words in the board.
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
# 
# Example:
# Input: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Output: ["eat","oath"]
# 
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
# Version: 1.0
# 11/14/18 by Jianfa
# ------------------------------

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0] or not words:
            return []
        
        res = []
        root = self.buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, root, res)
        
        return res
    
    def dfs(self, i, j, board, root, res):
        c = board[i][j]
        index = ord(c) - ord('a')
        if c == '#' or not root.links[index]:  # this unit is visited or it cannot be found in trie
            return
        
        root = root.links[index]
        if root.word:  # found a word
            res.append(root.word)
            root.word = ""  # avoid duplicate
        
        board[i][j] = '#'  # indicate this unit is visited
        # Do dfs in 4 directions
        if i > 0:
            self.dfs(i-1, j, board, root, res)
        if j > 0:
            self.dfs(i, j-1, board, root, res)
        if i < len(board) - 1:
            self.dfs(i+1, j, board, root, res)
        if j < len(board[0]) - 1:
            self.dfs(i, j+1, board, root, res)
        
        board[i][j] = c  # Set it back
    
    def buildTrie(self, words):
        root = TrieNode()
        for w in words:
            p = root
            for c in w:
                index = ord(c) - ord('a')
                if not p.links[index]:
                    p.links[index] = TrieNode()
                p = p.links[index]
            
            p.word = w
        
        return root
    
class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.word = ""

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow idea from https://leetcode.com/problems/word-search-ii/discuss/59780/Java-15ms-Easiest-Solution-(100.00)
# Main idea is to build a trie to record all words.
# Then start from every unit in the board, to find whether a specific word exists.