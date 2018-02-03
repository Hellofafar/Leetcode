# ------------------------------
# 89. Gray Code
# 
# Description:
# The gray code is a binary numeral system where two successive values differ in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray 
# code. A gray code sequence must begin with 0.
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# Note:
# For a given n, a gray code sequence is not uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
# 
# Version: 1.0
# 02/02/18 by Jianfa
# ------------------------------

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1 << n):
            res.append(i ^ i >> 1)
            
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Terrible problem.
# Idea from: https://leetcode.com/problems/gray-code/discuss/29881/An-accepted-three-line-solution-in-JAVA