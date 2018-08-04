# ------------------------------
# 680. Valid Palindrome II
# 
# Description:
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# Example 1:
# Input: "aba"
# Output: True
# 
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
# 
# Version: 1.0
# 08/03/18 by Jianfa
# ------------------------------

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True
        
        l = 0
        r = len(s) - 1
        deleted = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                
            else:
                if s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]:
                    return True
                
                else:
                    return False
        
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use two pointers. When a difference is met, check whether the rest part of substring is palindrome.