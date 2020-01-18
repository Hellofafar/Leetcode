# ------------------------------
# 526. Beautiful Arrangement
# 
# Description:
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array 
# that is constructed by these N numbers successfully if one of the following is true for 
# the ith position (1 <= i <= N) in this array:
# 
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# 
# Now given N, how many beautiful arrangements can you construct?
# 
# Example 1:
# 
# Input: 2
# Output: 2
# 
# Explanation: 
# The first beautiful arrangement is [1, 2]:
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# 
# The second beautiful arrangement is [2, 1]:
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# 
# Note:
# N is a positive integer and will not exceed 15.
# 
# Version: 1.0
# 01/17/19 by Jianfa
# ------------------------------

class Solution:
    count = 0
    
    def countArrangement(self, N: int) -> int:
        visited = [False] * (N + 1)
        def helper(N: int, pos: int) -> None:
            if pos > N:
                self.count += 1
                return

            for i in range(1, N+1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    helper(N, pos + 1)
                    visited[i] = False
        
        helper(N, 1)
        return self.count

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from Solution: https://leetcode.com/problems/beautiful-arrangement/solution/
# and https://leetcode.com/problems/beautiful-arrangement/discuss/99707/Java-Solution-Backtracking
# Key idea is to generate all possible permutations.
# 
# O(k) time complexity, k is the number of valid permutation
# O(n) space complexity