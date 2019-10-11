# ------------------------------
# 421. Maximum XOR of Two Numbers in an Array
# 
# Description:
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
# 
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# Could you do this in O(n) runtime?
# 
# Example:
# Input: [3, 10, 5, 25, 2, 8]
# Output: 28
# Explanation: The maximum result is 5 ^ 25 = 28.
# 
# Version: 1.0
# 10/10/19 by Jianfa
# ------------------------------

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxResult = 0
        mask = 0
        
        for i in range(32)[::-1]:
            mask = mask | (1 << i)
            
            leftSet = set()
            for n in nums:
                leftPartOfNum = n & mask
                leftSet.add(leftPartOfNum)
                
            greedyTry = maxResult | (1 << i)
            
            for leftPartOfNum in leftSet:
                if leftPartOfNum ^ greedyTry in leftSet:
                    # there exists two number can get greedyTry by XOR
                    maxResult = greedyTry
                    break
            
        return maxResult

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Bit manipulation solution from: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91049/Java-O(n)-solution-using-bit-manipulation-and-HashMap
# Explanation: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91049/Java-O(n)-solution-using-bit-manipulation-and-HashMap/95535