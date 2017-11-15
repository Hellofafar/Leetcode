# ------------------------------
# 246. Strobogrammatic Number
# 
# Description:
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# 
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# 
# For example, the numbers "69", "88", and "818" are all strobogrammatic.
# 
# Version: 1.0
# 11/14/17 by Jianfa
# ------------------------------

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        numDict = {0:0, 1:1, 6:9, 8:8, 9:6}
        if not num:
            return False
        
        left = 0
        right = len(num) - 1
        while left <= right:
            if int(num[left]) not in numDict or numDict[int(num[left])] != int(num[right]):
                return False
            left += 1
            right -= 1
        
        return True
        

# ------------------------------
# Summary:
# Use dictionary. Don't forget 0.