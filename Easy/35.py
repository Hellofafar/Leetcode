# ------------------------------
# 35. Search Insert Position
# 
# Description:
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# 
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
# 
# Version: 1.0
# 09/24/17 by Jianfa
# ------------------------------

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        temp = nums
        start = 0
        end = nums_len
        half = nums_len // 2
        while len(temp) > 0:
            if target == nums[start + half]:
                return start + half
            elif target < nums[start + half]:
                end = start + half
                temp = nums[start:end]
            else:
                start = start + half + 1
                temp = nums[start:end]
            
            half = len(temp) // 2
        
        return start

# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     nums = [1,3,5,6]
#     target = 0
    
#     print(test.searchInsert(nums, target))


# ------------------------------
# Summary:
# Ideas from other solution are similar, dividing array into two is commonly used.
# The difference is other solution set start = 0, end = len(nums) - 1, and mid = (left + right) / 2
# The mid is better than "half" used in my solution, which is more directly to locate the position.