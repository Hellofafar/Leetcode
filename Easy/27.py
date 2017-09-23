# ------------------------------
# 27. Remove Element
# 
# Description:
# Given an array and a value, remove all instances of that value in place and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# 
# Example:
# Given input array nums = [3,2,2,3], val = 3
# Your function should return length = 2, with the first two elements of nums being 2.
# 
# Version: 1.0
# 09/22/17 by Jianfa
# ------------------------------

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        list_len = len(nums)
        if list_len == 0:
            return list_len
        else:
            l = r = 0
            while r < list_len:
                if nums[r] != val:
                    nums[l] = nums[r]
                    l += 1
                r += 1

            return l


# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     nums = []
    
#     print(test.removeElement(nums, 4))


# ------------------------------
# Summary:
# I borrowed the idea from problem 26 that I used two pointers to do list updating, which is also the
# most usual solution.