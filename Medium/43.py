# ------------------------------
# 43. Multiply Strings
# 
# Description:
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
# 
# Version: 1.0
# 11/03/17 by Jianfa
# ------------------------------

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        
        res = [0 for x in range(l1 + l2)]
        
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                summ = mul + res[p2]
                
                res[p1] += summ / 10
                res[p2] = summ % 10
                
        s = ""
        for num in res:
            if not (s == "" and num == 0):
                s += str(num)
        
        return "0" if s == "" else s
                

# Used for test
if __name__ == "__main__":
    test = Solution()
    num1 = "0"
    num2 = "0"

    print(test.multiply(num1, num2))

# ------------------------------
# Summary:
# I mainly follow "Easiest JAVA Solution with Graph Explanation" in the discuss section.
# The idea is to start from right to left, perform multiplication on every pair of digits, and add them together.
# The key point is: num1[i] * num2[j] will be placed at indices [i + j, i + j + 1]