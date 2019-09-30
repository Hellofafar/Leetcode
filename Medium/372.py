# ------------------------------
# 372. Super Pow
# 
# Description:
# Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely 
# large positive integer given in the form of an array.
# 
# Example 1:
# Input: a = 2, b = [3]
# Output: 8
# 
# Example 2:
# Input: a = 2, b = [1,0]
# Output: 1024
# 
# Version: 1.0
# 09/29/19 by Jianfa
# ------------------------------

class Solution:
    def __init__(self):
        self.base = 1337
        
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        
        lastDigit = b.pop()
        return self.powMod(self.superPow(a, b), 10) * self.powMod(a, lastDigit) % self.base
        
    def powMod(self, a: int, k: int) -> int:
        result = 1
        for _ in range(k):
            result = (result * a) % self.base
        
        return result

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/super-pow/discuss/84472/C%2B%2B-Clean-and-Short-Solution
# One knowledge: ab % k = (a%k)(b%k)%k
# One observation:
# a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
# One formula using f:
# f(a,1234567) = f(a, 1234560) * f(a, 7) % k = f(f(a, 123456),10) * f(a,7)%k;