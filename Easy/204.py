# ------------------------------
# 204. Count Primes
# 
# Description:
# Count the number of prime numbers less than a non-negative number, n.
# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# Version: 1.0
# 06/11/18 by Jianfa
# ------------------------------

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        prime = [1] * n
        prime[0] = False
        prime[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(2, (n-1)/i + 1):
                    prime[i*j] = 0
        
        return sum(prime)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use hash map to tag every number so every one will be checked only once.