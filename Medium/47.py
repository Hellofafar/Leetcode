# ------------------------------
# 46. Permutations II
# 
# Description:
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# 
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
# 
# Version: 1.0
# 11/03/17 by Jianfa
# ------------------------------

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = self.backtrack(nums)
        return res
    
    def backtrack(self, nums):        
        if not nums:
            return [nums]
        
        res = []
        
        curr = [x for x in nums]
        for idx, i in enumerate(curr):
            if idx > 0 and i == curr[idx - 1]:
                continue
            temp = []
            rest = [curr[j] for j in range(len(curr)) if j != idx]
            temp = self.backtrack(rest)
            for item in temp:
                item.insert(0, i)
            res += temp
            
        return res


if __name__ == "__main__":
    test = Solution()
    nums = [1,1,2]

    print(test.permute(nums))

# ------------------------------
# Summary:
# Similar to 46.py, also using backtrack. The difference is when traverse the number in line 36, need to skip
# the same item. So I sort the nums at first and just pick the first item to backtrack if it has duplicates.