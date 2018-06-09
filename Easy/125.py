# ------------------------------
# 125. Valid Palindrome
# 
# Description:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# Example 2:
# Input: "race a car"
# Output: false
# 
# Version: 1.0
# 06/08/18 by Jianfa
# ------------------------------

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        h = 0
        e = len(s) - 1
        
        while h < e:
            if not 'A' <= s[h] <= 'Z' and not 'a' <= s[h] <= 'z' and not '0' <= s[h] <= '9' :
                h += 1
                continue
                
            if not 'A' <= s[e] <= 'Z' and not 'a' <= s[e] <= 'z' and not '0' <= s[e] <= '9':
                e -= 1
                continue
            
            if s[h].lower() == s[e].lower():
                h += 1
                e -= 1
            
            else:
                return False
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Number should also be considered.