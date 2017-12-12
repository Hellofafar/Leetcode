# ------------------------------
# 422. Valid Word Square
# 
# Description:
# Given a sequence of words, check whether it forms a valid word square.
# 
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 
# 0 ≤ k < max(numRows, numColumns).
# 
# Note:
# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.
# 
# Version: 1.0
# 12/11/17 by Jianfa
# ------------------------------

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if not words:
            return True
        
        n = len(words)
        for i in range(n):
            for j in range(len(words[i])):
                if j >= n or len(words[j]) <= i or words[i][j] != words[j][i]:
                    return False
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from "Java AC Solution Easy to Understand" in discuss section.
# The three conditions for false are worthwhile to understand clearly
# 1. Length of any word in words should be smaller than words length.
# 2. If there is ith word, then its previous word should have a length greater than i
# 3. words[i][j] == words[j][i], which is easy to understand.