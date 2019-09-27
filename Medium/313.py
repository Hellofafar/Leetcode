# ------------------------------
# 313. Super Ugly Number
# 
# Description:
# Write a program to find the nth super ugly number.
# 
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
# 
# Example:
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
#              super ugly numbers given primes = [2,7,13,19] of size 4.
# 
# Note:
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
# 
# Version: 1.0
# 09/26/19 by Jianfa
# ------------------------------

import sys

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
#         ugly = [0 for _ in range(n)]
#         length = len(primes)
#         idx = [0 for _ in range(length)]
        
#         ugly[0] = 1
#         for i in range(1, n):
#             ugly[i] = sys.maxsize
#             for j in range(length):
#                 ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
            
#             for j in range(length):
#                 while ugly[idx[j]] * primes[j] <= ugly[i]:
#                     idx[j] += 1
        
#         return ugly[n-1]
        
        ugly = [0 for _ in range(n)]
        length = len(primes)
        idx = [0 for _ in range(length)] # index of min number in the ugly that hasn't been multiplied by primes[j]
        val = [1 for _ in range(length)] # value of min number in the ugly that hasn't been multiplied by primes[j] multiply primes[j] 
        
        next = 1
        for i in range(n):
            ugly[i] = next
            next = sys.maxsize
            
            for j in range(length):
                if val[j] == ugly[i]:
                    val[j] = ugly[idx[j]] * primes[j]
                    idx[j] += 1
                next = min(next, val[j])
        
        return ugly[n-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/super-ugly-number/discuss/76291/Java-three-methods-23ms-36-ms-58ms(with-heap)-performance-explained
# Main idea is to generate a new ugly number by multiplying a prime with previous ugly number, while it is
# important to think about which previous ugly number should be multiplied.