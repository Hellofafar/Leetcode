# ------------------------------
# 541. Reverse String II
# 
# Description:
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]
# 
# Version: 1.0
# 07/14/18 by Jianfa
# ------------------------------

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        time = 0
        while time * k < len(s):
            temp = s[time*k:(time+2)*k]
            if len(temp) <= k:
                res += temp[::-1]
            
            else:
                res += temp[k-1::-1] + temp[k:]
            
            time += 2
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 