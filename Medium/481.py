# ------------------------------
# 481. Magical String
# 
# Description:
# A magical string S consists of only '1' and '2' and obeys the following rules:
# 
# The string S is magical because concatenating the number of contiguous occurrences of 
# characters '1' and '2' generates the string S itself.
# 
# The first few elements of string S is the following: S = "1221121221221121122……"
# If we group the consecutive '1's and '2's in S, it will be:
# 1 22 11 2 1 22 1 22 11 2 11 22 ......
# and the occurrences of '1's or '2's in each group are:
# 1 2 2 1 1 2 1 2 2 1 2 2 ......
# 
# You can see that the occurrence sequence above is the S itself.
# 
# Given an integer N as input, return the number of '1's in the first N number in the 
# magical string S.
# 
# Note: N will not exceed 100,000.
# 
# Example 1:
# Input: 6
# Output: 3
# Explanation: The first 6 elements of magical string S is "12211" and it contains three 
# 1's, so return 3.
# 
# Version: 1.0
# 10/22/19 by Jianfa
# ------------------------------

class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        
        a = [0] * (n + 1)  # n + 1 is to avoid overflow because the last round head might points to a number 2
        a[0], a[1], a[2] = 1, 2, 2
        head = 2  # head points to the number which will be used to generate new numbers
        tail = 3  # tail points to the next empty position to put the new number
        num = 1
        res = 1
        
        while tail < n: # keep generating new numbers until tail >= n
            for i in range(a[head]):
                a[tail] = num
                if num == 1 and tail < n:
                    res += 1
                tail += 1
            
            num = num ^ 3  # switch num from 1 to 2 or 2 to 1
            head += 1
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointer idea from https://leetcode.com/problems/magical-string/discuss/96413/Simple-Java-solution-using-one-array-and-two-pointers
# O(n) time, O(n) space