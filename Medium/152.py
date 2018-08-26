# ------------------------------
# 152. Maximum Product Subarray
# 
# Description:
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
# Version: 1.0
# 08/25/18 by Jianfa
# ------------------------------

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        r = nums[0]
        imax = r
        imin = r # imax/imin stores the max/min product of subarray that ends with the current number A[i]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax # multiplied by a negative makes big number smaller, small number bigger
            
            imax = max(nums[i], nums[i] * imax)
            imin = min(nums[i], nums[i] * imin)
            
            r = max(r, imax)
        
        return r

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# A very smart solution from https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity
# 
# imax & imin is the current max/min product of subarray ends with current number nums[i]
# Key point 1: when nums[i] < 0, swap imax and imin
# Key point 2: maintain r, r = max(r, imax)