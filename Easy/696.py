# ------------------------------
# c696. Count Binary Substrings (Weekly Contest 54)
# 
# Description:
# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's 
# and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# 
# Substrings that occur multiple times are counted the number of times they occur.
# 
# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", 
# "1100", "10", "0011", and "01".
# 
# Notice that some of these substrings repeat and are counted the number of times they occur.
# 
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
# 
# Version: 1.0
# 10/14/17 by Jianfa
# ------------------------------

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        
        l0 = l1 = 0
        
        if int(s[0]):
            flag = True
            l1 += 1
        else:
            flag = False
            l0 += 1
        
        pre_len = 0
        for idx, num in enumerate(s[1:]):
            if flag:
                if int(num):
                    l1 += 1
                    if l1 <= l0:
                        res += 1

                else:
                    flag = False
                    l0 = 1
                    res += 1
                    
            else:
                if not int(num):
                    l0 += 1
                    if l0 <= l1:
                        res += 1
                
                else:
                    flag = True
                    l1 = 1
                    res += 1
                    
        return res
        
        a = [1,2,3,4]
        b = a[a<2]

# ------------------------------
# Summary:
# 