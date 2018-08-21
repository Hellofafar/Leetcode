# ------------------------------
# 137. Single Number II
# 
# Description:
# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Example 1:
# Input: [2,2,3,2]
# Output: 3
# 
# Example 2:
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
# Version: 1.0
# 08/20/18 by Jianfa
# ------------------------------

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while nums:
            n = nums.pop(0)
            if n in nums:
                nums.remove(n)
                nums.remove(n)
            else:
                return n

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 