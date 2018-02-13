# ------------------------------
# 80. Remove Duplicates from Sorted Array II
# 
# Description:
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums being 
# 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
# 
# Version: 1.0
# 01/21/18 by Jianfa
# ------------------------------

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        slow = 0
        fast = 1
        count = 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                if count == 1:
                    slow += 1
                    nums[slow] = nums[fast]
                count += 1
                fast += 1
            
            else:
                slow += 1
                nums[slow] = nums[fast]    
                count = 1
                fast += 1
        
        return slow + 1
                

# Used for testing
if __name__ == "__main__":
    test = Solution()
    nums = [1,1]
    print(test.removeDuplicates(nums))

# ------------------------------
# Summary:
# Two pointer, one slow and one fast.