# ------------------------------
# 26. Remove Duplicates from Sorted Array
# 
# Description:
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# For example,
# Given input array nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
# 
# Version: 1.0
# 09/17/17 by Jianfa
# ------------------------------

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:            
            nums_len = len(nums)
            i = 0
            check = nums[0] - 1
            while i < nums_len:
                if check != nums[i]:
                    check = nums[i]
                    i += 1
                else:
                    nums.pop(i)
                    nums_len -= 1
            
            return len(nums)


# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [1,1,1,2,3,4,4,4,4]
    
    print(test.removeDuplicates(nums))


# ------------------------------
# Good idea from other solution:
# Actually there is no need to really remove value from the list. As the last sentence said
# "It doesn't matter what you leave beyond the new length." So we can just modify the first several
# numbers which is the length of unique values, but leave other values behind unchanged. We set two
# runner: a fast runner and a slow runner. As long as a different value is met, modify the corresponding 
# value in position of slow runner, otherwise move the fast runner.
# Here is a link for reference:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/