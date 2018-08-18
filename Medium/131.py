# ------------------------------
# 131. Palindrome Partitioning
# 
# Description:
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# Example:
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

# Version: 1.0
# 08/17/18 by Jianfa
# ------------------------------

class Solution(object):
    def __init__(self):
        self.res = []
        self.curList = []
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.backtrack(s, 0)
        return self.res
    
    def backtrack(self, s, l):
        if len(self.curList) > 0 and l >= len(s):
            temp = [x for x in self.curList]
            self.res.append(temp)
        
        for i in range(l, len(s)):
            if self.isPalindrome(s, l, i):
                self.curList.append(s[l:i+1])
                self.backtrack(s, i+1)
                self.curList.pop()
            
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Backtrack solution.
# Follow the idea from: https://leetcode.com/problems/palindrome-partitioning/discuss/41963/Java:-Backtracking-solution.