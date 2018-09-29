# ------------------------------
# 228. Summary Ranges
# 
# Description:
# 
# Version: 2.0
# 09/25/18 by Jianfa
# ------------------------------

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        
        The idea is use two pointers: left and right to record the data range.
        Go over the array, if current number equals to last number plus one, then the range is continuous; 
        otherwise, store the range and reset left and right pointer to current index.
        """
        if not nums:
            return []
        
        res = []
        left = right = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                right += 1
            else:
                if left == right:  # If there is only one number in this range
                    res.append('%d' % nums[left])
                else:              # If there are more than one numbers in this range
                    res.append('%d->%d' % (nums[left], nums[right]))
                left = right = i
        
        if left == right:          # Record the last range
            res.append('%d' % nums[left])
        else:
            res.append('%d->%d' % (nums[left], nums[right]))
        
        return res
        
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 