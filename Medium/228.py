# ------------------------------
# 228. Summary Ranges
# 
# Description:
# Given a sorted integer array without duplicates, return the summary of its ranges.
# 
# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# 
# Version: 1.0
# 12/11/17 by Jianfa
# ------------------------------

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        res = []
        s = nums[0]
        e = nums[0]
        
        for x in nums[1:]:
            if x - e == 1:
                e = x
            else:
                if s == e:
                    res.append(str(s))
                else:
                    res.append("%d->%d" % (s, e))
                s = x
                e = x
        
        if s == e:
            res.append(str(s))
        else:
            res.append("%d->%d" % (s, e))
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Initialize s and e, then check from the second item in array one by one. If a new item is more than 1 greater
# than the previous, add a new summary to result list.
# Finally add the last summary string to the result.