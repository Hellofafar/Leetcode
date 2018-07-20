# ------------------------------
# 581. Shortest Unsorted Continuous Subarray
# 
# Description:
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# 
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.
# 
# Version: 1.0
# 07/19/18 by Jianfa
# ------------------------------

import bisect

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = len(nums)
        right = 0
        tempMax = nums[0]
        for idx, n in enumerate(nums):
            if n < tempMax:
                if left == len(nums):
                    left = bisect.bisect(nums[:idx], n)
                
                else:
                    if n < nums[left]:
                        temp = bisect.bisect(nums[:left], n)
                        if temp < left:
                            left = temp
                
                right = idx
            
            else:
                tempMax = n
        
        if right > left:
            return right - left + 1
        
        else:
            return 0

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Find the left index of subarray to be sorted at first, then find the right index of subarray.
# Note that the left index may always be updated, so need to check every time when n < tempMax.