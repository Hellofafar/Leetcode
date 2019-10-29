# ------------------------------
# 523. Continuous Subarray Sum
# 
# Description:
# Given a list of non-negative numbers and a target integer k, write a function to check if 
# the array has a continuous subarray of size at least 2 that sums up to a multiple of k, 
# that is, sums up to n*k where n is also an integer.
# 
# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# 
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
# 
# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
# 
# Version: 1.0
# 10/28/19 by Jianfa
# ------------------------------

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modDict = {0: -1} # if an array sums up to n*k, an initial value is required
        runningSum = 0
        for i, n in enumerate(nums):
            runningSum += n
            if k != 0:
                runningSum %= k
            
            if runningSum in modDict:
                # for i > j, if sum(i) % k == sum(j) % k
                # (sum(i) - sum(j)) % k == 0, then just check the size
                # of subarray (j, i]
                if i - modDict[runningSum] > 1:
                    return True
            else:
                modDict[runningSum] = i
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Map solution from https://leetcode.com/problems/continuous-subarray-sum/discuss/99499/Java-O(n)-time-O(k)-space
# iterate through the input array exactly once, keeping track of the running sum mod k of 
# the elements in the process. If we find that a running sum value at index j has been 
# previously seen before in some earlier index i in the array, then we know that the 
# sub-array (i,j] contains a desired sum.
# 
# O(n) time, O(k) space