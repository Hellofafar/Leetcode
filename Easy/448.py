# ------------------------------
# 448. Find All Numbers Disappeared in an Array
# 
# Description:
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [5,6]
# 
# Version: 1.0
# 07/06/18 by Jianfa
# ------------------------------

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            if nums[abs(i) - 1] > 0:
                nums[abs(i)- 1] *= -1  
            
        for j in range(len(nums)):
            if nums[j] > 0:
                res.append(j+1)
                
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# It's very smart solution from https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92956/Java-accepted-simple-solution