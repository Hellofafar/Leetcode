# ------------------------------
# 31. Next Permutation
# 
# Description:
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
# 
# Version: 1.0
# 10/19/17 by Jianfa
# ------------------------------

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        while nums_len > 1:
            if nums[nums_len - 1] <= nums[nums_len - 2]:
                nums_len -= 1
            else:
                swap_i = nums_len - 2
                swap_j = len(nums) - 1
                if swap_i < len(nums) - 2:
                    for idx, n in enumerate(nums[swap_i + 1:]):
                        if n <= nums[swap_i]:
                            swap_j = swap_i + idx
                            break
                nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]
                swap_s = swap_i + 1
                swap_e = len(nums) - 1
                while swap_s < swap_e:
                    nums[swap_s], nums[swap_e] = nums[swap_e], nums[swap_s]
                    swap_s += 1
                    swap_e -= 1
                break
        
        if nums_len == 1:
            nums.sort()
                

# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [1,3,2]
    
    test.nextPermutation(nums)
    print(nums)

# ------------------------------
# Summary:
# The idea is, from the last item move backward and check, until finding an item that is less than previous item.
# Swap this item with a smallest larger item within the items just checked.
# For example the list is [4,6,2,7,8,12,9,4,3,1]. Then 8 and 9 are the items to be swapped.
# After the first swap, it became [4,6,2,7,9,12,8,4,3,1]. Then all need to do is sort [12,8,4,3,1]. I swap the
# corresponding pairs to sort.