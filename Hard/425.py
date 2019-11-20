# ------------------------------
# 425. Word Squares
# 
# Description:
# Given a set of words (without duplicates), find all word squares you can build from them.
# 
# A sequence of words forms a valid word square if the kth row and column read the exact 
# same string, where 0 ≤ k < max(numRows, numColumns).
# 
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because 
# each word reads the same both horizontally and vertically.
# 
# b a l l
# a r e a
# l e a d
# l a d y
# 
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# 
# Example 1:
# Input:
# ["area","lead","wall","lady","ball"]
# 
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# 
# Example 2:
# Input:
# ["abat","baba","atan","atal"]
# 
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# 
# Version: 1.0
# 11/19/19 by Jianfa
# ------------------------------

class TrieNode:
    def __init__(self):
        self.startWith = [] # list of words start with this prefix
        self.children = [None] * 26
        
class Solution:
    wordLen = 0
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words or not words[0]:
            return []
        
        self.wordLen = len(words[0]) # word length
        trie = self.buildTrie(words) # get TRIE
        
        res = []
        # index: index of character in the words form the prefix
        # wordSquare: current candidate wordSquare
        def backtrack(index, wordSquare):
            if index == self.wordLen:
                res.append(wordSquare[:])
                return
            
            prefix = "".join([w[index] for w in wordSquare])
            candidates = self.findWordsWithPrefix(trie, prefix)
            for c in candidates:
                wordSquare.append(c)
                backtrack(index+1, wordSquare)
                wordSquare.pop()
        
        for w in words:
            # traverse every word to start backtrack process
            word_square = [w]
            backtrack(1, word_square)
        
        return res
    
    def buildTrie(self, words):
        trie = TrieNode()
        for w in words:
            p = trie
            for c in w:
                index = ord(c) - 97
                if p.children[index] is None:
                    p.children[index] = TrieNode()
                p = p.children[index]
                p.startWith.append(w)
        
        return trie
    
    def findWordsWithPrefix(self, root, prefix):
        # find all words start with prefix
        for c in prefix:
            index = ord(c) - 97
            if root.children[index] is not None:
                root = root.children[index]
            else:
                # no word starts with this prefix
                return []
        return root.startWith

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Backtrack + TRIE
# Idea from https://leetcode.com/problems/word-squares/discuss/91333/Explained.-My-Java-solution-using-Trie-126ms-1616
# and https://leetcode.com/problems/word-squares/solution/
# 
# Build a TRIE at first, then do backtrack to check all possibilities.
# 
# O(N * 26^L * L) time, N is number of words and L is length of a single word