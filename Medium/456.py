# ------------------------------
# 456. 132 Pattern
# 
# Description:
# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak 
# such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers 
# as input and checks whether there is a 132 pattern in the list.
# 
# Note: n will be less than 15,000.
# 
# Example 1:
# Input: [1, 2, 3, 4]
# Output: False
# Explanation: There is no 132 pattern in the sequence.
# 
# Example 2:
# Input: [3, 1, 4, 2]
# Output: True
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# 
# Example 3:
# Input: [-1, 3, 2, 0]
# Output: True
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
# 
# Version: 1.0
# 10/15/19 by Jianfa
# ------------------------------

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = -sys.maxsize
        stack = []  # candidates of s3
        
        for i in range(len(nums)-1, -1, -1):
            # if nums[i] < s3, actually it also means nums[i] < s2
            # s2 is currently stored in stack
            if nums[i] < s3:
                return True
            
            # find new candidate of S3, which is largest in the stack
            while stack and stack[-1] < nums[i]:
                s3 = stack.pop()
            
            stack.append(nums[i])
            
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/132-pattern/discuss/94071/Single-pass-C%2B%2B-O(n)-space-and-time-solution-(8-lines)-with-detailed-explanation.
# INTUITION: Suppose we want to find a 123 sequence with s1 < s2 < s3, we just need to find s3, 
# followed by s2 and s1. Now if we want to find a 132 sequence with s1 < s3 < s2, we need to 
# switch up the order of searching. we want to first find s2, followed by s3, then s1. 
# 
# O(n) time and O(n) space