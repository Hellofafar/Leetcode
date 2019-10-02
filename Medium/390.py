# ------------------------------
# 390. Elimination Game
# 
# Description:
# There is a list of sorted integers from 1 to n. Starting from left to right, remove the 
# first number and every other number afterward until you reach the end of the list.
# 
# Repeat the previous step again, but this time from right to left, remove the right most 
# number and every other number from the remaining numbers.
# 
# We keep repeating the steps again, alternating left to right and right to left, until a 
# single number remains.
# 
# Find the last number that remains starting with a list of length n.
# 
# Example:
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
# 
# Output:
# 6
# 
# Version: 1.0
# 10/01/19 by Jianfa
# ------------------------------

class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True  # Alternate from left to right
        remaining = n  # Remaining numbers count
        step = 1
        head = 1
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            step *= 2
            remaining //= 2
            left = not left
        
        return head

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# O(logN) solution from: https://leetcode.com/problems/elimination-game/discuss/87119/JAVA%3A-Easiest-solution-O(logN)-with-explanation
# update and record head in each turn. when the total number becomes 1, head is the only number left.
# head be updated only when
# - if we move from left
# - if we move from right and the total remaining number % 2 == 1
# like 2 4 6 8 10, we move from 10, we will take out 10, 6 and 2, head is deleted and move to 4
# like 2 4 6 8 10 12, we move from 12, we will take out 12, 8, 4, head is still remaining 2