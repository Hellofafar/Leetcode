# ------------------------------
# 315. Count of Smaller Numbers After Self
# 
# Description:
# You are given an integer array nums and you have to return a new counts array. The counts 
# array has the property where counts[i] is the number of smaller elements to the right of nums[i].
# 
# Example:
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# Version: 1.0
# 11/18/19 by Jianfa
# ------------------------------

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sortEnum(enum):
            half = len(enum) // 2
            if half:
                left, right = sortEnum(enum[:half]), sortEnum(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        # smaller number on the left, larger number on the right
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        
        smaller = [0] * len(nums)
        enums = list(enumerate(nums))
        sortEnum(enums)
        return smaller

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Merge sort solution from: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
# Key idea is the smaller numbers on the right of a number are exactly those that jump from 
# its right to its left during a stable sort. So I do mergesort with added tracking of those 
# right-to-left jumps.
# 
# O(N * logN) time