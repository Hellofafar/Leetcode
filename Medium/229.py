# ------------------------------
# 229. Majority Element II
# 
# Description:
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.
# Example 1:
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
# Version: 1.0
# 09/26/18 by Jianfa
# ------------------------------

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        since the requirement is finding the majority for more than ceiling of [n/3], 
        the answer would be less than or equal to two numbers.
        """
        if not nums:
            return []
        
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        for i in (candidate1, candidate2):
            if nums.count(i) > len(nums) / 3:
                res.append(i)
        
        return res
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration
# Boyer-Moore Majority Vote algorithm: http://goo.gl/64Nams