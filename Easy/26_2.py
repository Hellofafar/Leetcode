# ------------------------------
# 26. Remove Duplicates from Sorted Array
# 
# Description:
# 
# 
# Version: 2.0
# 11/12/19 by Jianfa
# ------------------------------

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curr = 0 # index of current unique element put in modified nums
        i = 1
        while i < len(nums):
            if nums[i] != nums[curr]:
                curr += 1
                nums[curr] = nums[i]
            i += 1
        
        return curr + 1 # total length of unique elements

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Record the index of last unique element. When a new unique element is found, move it right
# after the last element, then update the index.
# 
# O(N) time O(1) space