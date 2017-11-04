# ------------------------------
# 46. Permutations
# 
# Description:
# Given a collection of distinct numbers, return all possible permutations.
# 
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# 
# Version: 1.0
# 11/03/17 by Jianfa
# ------------------------------

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """     
        res = self.backtrack(nums)
        return res
    
    def backtrack(self, nums):        
        if not nums:
            return [nums]
        
        res = []
        
        curr = [x for x in nums]
        for i in curr:
            temp = []
            rest = [x for x in curr if x != i]
            temp = self.backtrack(rest)
            for item in temp:
                item.insert(0, i)
            res += temp
            
        return res


# Used for test
if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3]

    print(test.permute(nums))

# ------------------------------
# Summary:
# Using backtrack. The difference to combinations is that permutations result does not append a complete list/tuple
# at a time, but uses backtrack function to insert number once a time for all current items.
# Note: when nums is [], return [[]]