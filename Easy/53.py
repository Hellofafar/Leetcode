# ------------------------------
# 53. Maximum Subarray
# 
# Description:
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# Version: 1.0
# 10/01/17 by Jianfa
# ------------------------------

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        current = 0
        for idx, n in enumerate(nums):
            if idx == 0:
                max_sum = n
                current = n

            else:
                current = max(n, current+n)

                if current > max_sum:
                    max_sum = current
        
        return max_sum


# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     nums = [-2,1,-3,4,-1,2,1,-5,4]
# 
#     print(test.maxSubArray(nums))


# ------------------------------
# Summary:
# The simple O(n) solution, may improve it with devide and conquar in the future.