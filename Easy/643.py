# ------------------------------
# 643. Maximum Average Subarray I
# 
# Description:
# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# Version: 1.0
# 07/28/18 by Jianfa
# ------------------------------

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxavg = float(sum(nums[:k])) / k
        cursum = sum(nums[:k])
        for i in range(k, len(nums)):
            cursum = cursum + nums[i] - nums[i-k]
            maxavg = max(maxavg, float(cursum) / k)
            
        
        return maxavg


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Sliding window solution. I at first added a if statement before maxavg "if nums[i] > nums[i-k]",
# but I met time out error.