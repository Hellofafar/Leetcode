# ------------------------------
# 525. Contiguous Array
# 
# Description:
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
# 
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# 
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# 
# Note: The length of the given binary array will not exceed 50,000.
# 
# Version: 1.0
# 01/16/20 by Jianfa
# ------------------------------

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        countMap = {0:-1} # initialize the countMap
        
        count = 0
        maxLen = 0
        for i, n in enumerate(nums):
            count = count - 1 if n == 0 else count + 1
            
            if count in countMap:
                maxLen = max(maxLen, i - countMap[count])
            else:
                countMap[count] = i
        
        return maxLen

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from Solution and https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
# Key idea is to use a dictionary to record the sum of array, if the sum appeared in the 
# dictionary before it means subarray between these two sum's index has equal numbers of 1 and 0.