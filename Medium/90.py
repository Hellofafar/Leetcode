# ------------------------------
# 90. Subsets II
# 
# Description:
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power 
# set).
# Note: The solution set must not contain duplicate subsets.
# 
# For example,
# If nums = [1,2,2], a solution is:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# 
# Version: 1.0
# 02/06/18 by Jianfa
# ------------------------------

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        totalset = [[]]
        nums.sort()
        i = 0
        while i < len(nums):
            count = 0
            while i + count < len(nums) and nums[i + count] == nums[i]:
                count += 1
            
            for j in range(len(totalset)):
                temp = [x for x in totalset[j]]
                for j in range(count):
                    temp.append(nums[i])
                    temp2 = [x for x in temp]
                    totalset.append(temp2)
                
            i += count
        
        return totalset

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Very smart solution from: https://leetcode.com/problems/subsets-ii/discuss/30168/C++-solution-and-explanation
# Basic idea as follows:
# 1. Check the number of a specific element, noted as "count"
# 2. For every subset in totalset, add current element to the subset different times to form a new set, and add 
# this new set to totalset.
# 3. Jump to next element.