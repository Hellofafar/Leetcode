# ------------------------------
# 70. Climbing Stairs
# 
# Description:
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 
# Note: Given n will be a positive integer.
# Example 1:
# Input: 2
# Output:  2
# 
# Explanation:  There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# Example 2:
# Input: 3
# Output:  3
# 
# Explanation:  There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# Version: 1.0
# 01/18/18 by Jianfa
# ------------------------------

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        steps = {}
        steps[1] = 1
        steps[2] = 2
        start = 3
        while start <= n:
            steps[start] = steps[start-1] + steps[start-2]
            start += 1
        
        return steps[n]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic solution.
# At first I tried to use recursive solution by return climbStairs(n-1) + climbStairs(n-2), it
# exceeds the time limit. Because it redundantly calculates some value during recursion.
# So I try to store climbStairs(n) value dynamically from very begining(1), until the n. In this
# process, climbStairs(n) will only be called once for each n.