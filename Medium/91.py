# ------------------------------
# 91. Decode Ways
# 
# Description:
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# 
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# The number of ways decoding "12" is 2.
# 
# Version: 1.0
# 02/19/18 by Jianfa
# ------------------------------

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        length = len(s)
        count = [0 for i in range(length+1)]
        count[length] = 1
        count[length-1] = 1 if int(s[length-1]) != 0 else 0
        
        for i in range(length-1)[::-1]:
            if s[i] == '0':
                count[i] = 0
            else:
                count[i] = count[i+1] + count[i+2] if int(s[i:i+2]) <= 26 else count[i+1]
        
        return count[0]

# Used for testing
if __name__ == "__main__":
    test = Solution()
    s = "01"

# ------------------------------
# Summary:
# DP solution. Get idea from: https://leetcode.com/problems/decode-ways/discuss/30357/DP-Solution-(Java)-for-reference
# An edge case is when s[i] == '0', count[i] should be 0.