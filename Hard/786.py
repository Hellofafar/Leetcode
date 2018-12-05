# ------------------------------
# 786. K-th Smallest Prime Fraction
# 
# Description:
# A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.
# What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.
# 
# Examples:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]
# 
# Explanation:
# The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# The third fraction is 2/5.
# 
# Input: A = [1, 7], K = 1
# Output: [1, 7]
# 
# Note:
# A will have length between 2 and 2000.
# Each A[i] will be between 1 and 30000.
# K will be between 1 and A.length * (A.length - 1) / 2.
# 
# Version: 1.0
# 12/05/18 by Jianfa
# ------------------------------

from fractions import Fraction

class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        def under(x):
            count = best = 0
            i = -1
            for j in range(1, len(A)):
                while A[i+1] < A[j] * x:
                    i += 1
                count += i+1
                if i >= 0:
                    best = max(best, Fraction(A[i], A[j]))
            
            return count, best
        
        lo, hi = 0.0, 1.0
        
        while hi - lo > 1e-9:
            mi = (hi + lo) / 2
            count, best = under(mi)
            if count < K:
                lo = mi
            else:
                res = best
                hi = mi
        
        return [res.numerator, res.denominator]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Binary search solution. Find the number of fractions less than x and the largest number less than x.
# When the number of fractions is K, then return the largest number less than x.
# Since K will be between 1 and A.length * (A.length - 1) / 2, all fractions should be less than 1.
# Idea from Solution section.