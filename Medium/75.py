# ------------------------------
# 75. Sort Colors
# 
# Description:
# Implement pow(x, n).
# 
# Version: 1.0
# 10/06/17 by Jianfa
# ------------------------------

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        l = 0
        while l < len(nums) and nums[l] == 0:
            l += 1
        
        r = len(nums) - 1
        while r >= 0 and nums[r] == 2:
            r -= 1
               
        i = l
        while i <= r:
            if nums[i] == 0:        
                nums[i] = nums[l]
                nums[l] = 0
                l += 1
                i += 1

            elif nums[i] == 2:
                nums[i] = nums[r]
                nums[r] = 2
                r -= 1
            
            else:
                i += 1
                
            
# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [2,0]

    test.sortColors(nums)

    print(nums)

# ------------------------------
# Summary:
# O(n) solution.
# Set l, i, r pointer. Move l forward to the first position that is not 0, move r backward to the first position
# that is not 2.
# While i <= r, do judgement
#     if meeting a "0", exchange number in l and i, then move 1 step both l and i (note)
#     if meeting a "1", move i
#     if meeting a "2", exchange number in r and i, then just move r 1 step back!! (just r) 