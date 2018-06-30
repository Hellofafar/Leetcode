# ------------------------------
# 409. Longest Palindrome
# 
# Description:
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.
# Note:
# Assume the length of given string will not exceed 1,010.
# Example:
# Input:
# "abccccdd"
# Output:
# 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# Version: 1.0
# 06/29/18 by Jianfa
# ------------------------------

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set(s)
        length = 0
        flag = 0
        for c in charset:
            if s.count(c) % 2 == 0:
                length += s.count(c)
            
            else:
                length += s.count(c) - 1
                flag = 1
        
        return length + flag

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 