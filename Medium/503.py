# ------------------------------
# 503. Next Greater Element II
# 
# Description:
# Given a circular array (the next element of the last element is the first element of the array), 
# print the Next Greater Number for every element. The Next Greater Number of a number x is the 
# first greater number to its traversing-order next in the array, which means you could search 
# circularly to find its next greater number. If it doesn't exist, output -1 for this number.
# 
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.
# 
# Note: The length of given array won't exceed 10000.
# 
# Version: 1.0
# 10/25/19 by Jianfa
# ------------------------------

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        size = len(nums)
        stack = [] # stores the previous greater elements on the right of nums[i]
        res = [0] * size
        # Go through the stack the first pass
        for i in range(size)[::-1]:
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1]
            stack.append(nums[i])
        # Go through the second pass
        for i in range(size)[::-1]:
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1]
            stack.append(nums[i])
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Stack solution from https://leetcode.com/problems/next-greater-element-ii/solution/
# Traverse the nums array two times from right to left