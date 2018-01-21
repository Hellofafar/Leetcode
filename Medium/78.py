# ------------------------------
# 78. Subsets
# 
# Description:
# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# 
# For example,
# If nums = [1,2,3], a solution is:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# 
# Version: 1.0
# 01/20/18 by Jianfa
# ------------------------------

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        result = []
        for i in range(len(nums) + 1):
            result += self.combine(nums, i)
            
        return result
        
    def combine(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """        
        res = []
        currlist = []
        self.backtrack(nums, k, currlist, 0, res)
        return res
        
    
    def backtrack(self, nums, k, currlist, start, res):
        if len(currlist) == k:
            temp = [x for x in currlist]
            res.append(temp)
        
        elif len(nums) - start + len(currlist) < k:
            return
        
        else:
            for i in range(start, len(nums)):
                currlist.append(nums[i])
                self.backtrack(nums, k, currlist, i+1, res)
                currlist.pop()
        

# Used for testing
if __name__ == "__main__":
    test = Solution()
    nums = [1,3,5]
    test.subsets(nums)

# ------------------------------
# Summary:
# Borrow the combine idea from 77.py. The major difference is here a number list is provided.
# The number list may include discontinuous integers. So the parameter "start" here means index 
# rather than number itself.