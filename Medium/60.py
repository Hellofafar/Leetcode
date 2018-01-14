# ------------------------------
# 60. Permutation Sequence
# 
# Description:
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# Note: Given n will be between 1 and 9 inclusive.
# 
# Version: 1.0
# 01/13/18 by Jianfa
# ------------------------------

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return ""
        
        factorials = [1]
        sum = 1
        for i in range(1, n+1):
            sum *= i
            factorials.append(sum)
        
        nums = [j for j in range(1, n+1)]
        
        res = ""
        k -= 1
        for i in range(1, n+1):
            idx = k / factorials[n-i]
            k -= idx * factorials[n-i]
            res += str(nums[idx])
            nums.pop(idx)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()
    n = 4
    k = 14
    print(test.getPermutation(n, k))

# ------------------------------
# Summary:
# Follow the idea from https://leetcode.com/problems/permutation-sequence/discuss/22507
# Implemented in python.