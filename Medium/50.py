# ------------------------------
# 50. Pow(x, n)
# 
# Description:
# Implement pow(x, n).
# 
# Version: 1.0
# 10/06/17 by Jianfa
# ------------------------------

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return self.myPow(1.0 / x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        else:
            temp_res = self.myPow(x, n // 2)
            if n % 2 == 0:              
                return temp_res * temp_res
            else:
                return temp_res * temp_res * x
             

# Used for test
if __name__ == "__main__":
    test = Solution()
    x = 8.88023
    n = 3

    print(test.myPow(x, n))

# ------------------------------
# Summary:
# O(logN) solution.
# Use recursion to calculate. Some special points need to be cared: 1. when n < 0; 2. when n % 2 == 0