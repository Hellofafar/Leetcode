# ------------------------------
# 368. Largest Divisible Subset
# 
# Description:
# Given a set of distinct positive integers, find the largest subset such that every pair 
# (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# 
# Example 2:
# Input: [1,2,4,8]
# Output: [1,2,4,8]
# 
# Version: 1.0
# 09/28/19 by Jianfa
# ------------------------------

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [1 for _ in range(n)]  # size of largest subset in which ith number is largest number
        pre = [-1 for _ in range(n)]  # index of largest divisor of ith number in the subset
        nums.sort()
        
        maxSize = 0
        index = -1
        for i in range(n):
            for j in range(i)[::-1]:
                if nums[i] % nums[j] == 0:  # Check if it's a divisor
                    if count[j] + 1 > count[i]:
                        count[i] = count[j] + 1
                        pre[i] = j  # record the index of divisor
            
            if count[i] > maxSize:
                maxSize = count[i]
                index = i
        
        ret = []
        while index != -1:
            ret.append(nums[index])
            index = pre[index]
        
        return ret

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/largest-divisible-subset/discuss/84006/Classic-DP-solution-similar-to-LIS-O(n2)
# Main idea is dp solution, from smaller number, build the subset containing the number and count the size of subset.
# Traverse all the number less than it and check if it's divisor.