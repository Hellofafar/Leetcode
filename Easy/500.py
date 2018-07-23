# ------------------------------
# 500. Keyboard Row
# 
# Description:
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
# 
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# Version: 1.0
# 07/10/18 by Jianfa
# ------------------------------

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        
        res = []
        for w in words:
            if set(w.lower()).issubset(row1) or set(w.lower()).issubset(row2) or set(w.lower()).issubset(row3):
                res.append(w)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The smart point here is using set.issubset()
# Idea from https://leetcode.com/problems/keyboard-row/discuss/97913/Easy-understand-solution-in-7-lines-for-everyone