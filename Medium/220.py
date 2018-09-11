# ------------------------------
# 220. Contains Duplicate III
# 
# Description:
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# Version: 1.0
# 09/10/18 by Jianfa
# ------------------------------

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        
        length = len(nums)
        width = t + 1
        bucket = {}
        
        for i in range(len(nums)):
            b = nums[i] / width
            if b in bucket:
                return True
            if b - 1 in bucket and abs(nums[i] - bucket[b-1]) <= t:
                return True
            if b + 1 in bucket and abs(nums[i] - bucket[b+1]) <= t:
                return True
            
            bucket[b] = nums[i]
            if i >= k:
                del bucket[nums[i-k] / width]
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Bucket sort solution from: https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets