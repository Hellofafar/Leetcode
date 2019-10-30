# ------------------------------
# 670. Maximum Swap
# 
# Description:
# Given a non-negative integer, you could swap two digits at most once to get the 
# maximum valued number. Return the maximum valued number you could get.
# 
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# 
# Note:
# The given number is in the range [0, 108]
# 
# Version: 2.0
# 10/29/19 by Jianfa
# ------------------------------

class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num)))           # get a list of integer (digits of num)
        last = {x: i for i, x in enumerate(A)} # last index of integer in the num
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, -1) > i:        # find the largest number which is larger than itsele to swap with
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Greedy solution from: https://leetcode.com/problems/maximum-swap/solution/