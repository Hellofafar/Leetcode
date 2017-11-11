# ------------------------------
# 163. Missing Ranges
# 
# Description:
# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return 
# its missing ranges.
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
# 
# 
# Version: 1.0
# 11/10/17 by Jianfa
# ------------------------------

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower not in nums:
            nums.insert(0, lower - 1)  # Note: insert lower - 1 here, which is used to detect whether lower exists
        
        if upper not in nums:
            nums.insert(len(nums), upper + 1)  # Note: insert upper + 1 here, to detect upper
            
        res = []
        for i, n in enumerate(nums[:-1]):  # i doesn't include last item (upper + 1)
            if nums[i+1] - nums[i] == 2:
                res.append(str(n+1))
                
            elif nums[i+1] - nums[i] > 2:
                res.append(str(n+1) + "->" + str(nums[i+1] - 1))
        
        return res
        

# ------------------------------
# Summary: