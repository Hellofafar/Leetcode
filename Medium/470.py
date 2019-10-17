# ------------------------------
# 470. Implement Rand10() Using Rand7()
# 
# Description:
# Given a function rand7 which generates a uniform random integer in the range 1 to 7, 
# write a function rand10 which generates a uniform random integer in the range 1 to 10.
# 
# Do NOT use system's Math.random().
# 
# Example 1:
# Input: 1
# Output: [7]
# 
# Example 2:
# Input: 2
# Output: [8,4]
# 
# Example 3:
# Input: 3
# Output: [8,1,10]
# 
# Note:
# rand7 is predefined.
# Each testcase has one argument: n, the number of times that rand10 is called.
# 
# Follow up:
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
# 
# Version: 1.0
# 10/16/19 by Jianfa
# ------------------------------

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = 41
        # The desired range is 1 - 40 using two times of rand7()
        while idx > 40:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
        
        return idx % 10 + 1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Rejection Sampling solution from https://leetcode.com/problems/implement-rand10-using-rand7/solution/
# Intuition is what if you want to generate a random integer in the range 1-49? How to generate a random
# number in the range of 1-10?
# 
# For follow up question, in range 41-49 it's distributed uniformly, so we can do rand7() again to get
# uniform distribution of 1-63. If 61-63 is chosen, then do rand7() again to get 1-21. If 21 is chosen, 
# then repeat the entire process.
# 
# O(1) average time, O(∞) worst case