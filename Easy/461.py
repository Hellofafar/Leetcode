# ------------------------------
# 461. Hamming Distance
# 
# Description:
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.
# Note:
# 0 ≤ x, y < 231.
# Example:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are different.
# 
# Version: 1.0
# 07/07/18 by Jianfa
# ------------------------------

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xs = bin(x)[2:]
        ys = bin(y)[2:]
        
        i = len(xs) - 1
        j = len(ys) - 1
        res = 0
        while i >= 0 and j >= 0:
            res += int(xs[i]) ^ int(ys[j])
            i -= 1
            j -= 1
        
        if i >= 0:
            res += xs[:i+1].count('1')
        
        if j >= 0:
            res += ys[:j+1].count('1')
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Actually the simplest way is: bin(x^y).count('1')