# ------------------------------
# 219. Contains Duplicate II
# 
# Description:
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# Version: 1.0
# 06/12/18 by Jianfa
# ------------------------------

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexDict = {}
        for i in range(len(nums)):
            if nums[i] in indexDict:
                if i - indexDict[nums[i]] <= k:
                    return True
                
            indexDict[nums[i]] = i
            
        return False
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 