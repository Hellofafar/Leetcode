# ------------------------------
# 506. Relative Ranks
# 
# Description:
# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
# For the left two athletes, you just need to output their relative ranks according to their scores.
# 
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
# 
# Version: 1.0
# 07/13/18 by Jianfa
# ------------------------------

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        sortNums = sorted(nums, reverse=True)
        for i in nums:
            idx = sortNums.index(i)
            if idx == 0:
                res.append('Gold Medal')
            
            elif idx == 1:
                res.append('Silver Medal')
            
            elif idx == 2:
                res.append('Bronze Medal')
            
            else:
                res.append(str(idx+1))
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 