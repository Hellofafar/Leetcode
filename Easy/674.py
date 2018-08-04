# ------------------------------
# 674. Longest Continuous Increasing Subsequence
# 
# Description:
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
# 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
# 
# Note: Length of the array will not exceed 10,000.
# Version: 1.0
# 08/03/18 by Jianfa
# ------------------------------

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 1
        curlen = 1
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                curlen += 1
            
            else:
                maxlen = max(maxlen, curlen)
                curlen = 1
        
        maxlen = max(maxlen, curlen)
        return maxlen

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 