# ------------------------------
# 163. Missing Ranges
# 
# Description:
# 
# Version: 2.0
# 11/03/18 by Jianfa
# ------------------------------

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        prev = lower - 1
        nums.append(upper+1)  # Add a element to help check edge case
        
        for i in nums:
            if i == prev:  # There may be duplicates
                continue
                
            if i != prev + 1:
                if i - prev == 2:  # if only 1 element is missing between prev and i
                    res.append("%d" % (i - 1))
                
                else:
                    res.append("%d->%d" % (prev + 1, i - 1))
                    
            prev = i
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Take care of situation when duplicate numbers exist in the nums.