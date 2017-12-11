# ------------------------------
# 248. Strobogrammatic Number III
# 
# Description:
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.
# 
# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.
# Note:
# Because the range might be a large number, the low and high numbers are represented as string.
# 
# Version: 1.0
# 12/10/17 by Jianfa
# ------------------------------

import bisect

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        low_len = len(low)
        high_len = len(high)
        result = []
        for i in range(low_len, high_len + 1):
            result.extend(self.helper(i, i))
            
        for idx, x in enumerate(result):
            result[idx] = int(x)
        
        low = int(low)
        high = int(high)
        
        result.sort()
        low_index = bisect.bisect_left(result, low)
        high_index = bisect.bisect(result, high)
        return high_index - low_index
        
        
    def helper(self, m, n):
        if m == 0:
            return [""]
        
        elif m == 1:
            return ["0", "1", "8"]
        
        else:
            temp = self.helper(m-2, n)
            res = []
            for item in temp:
                if m != n:
                    res.append("0" + item + "0")
                res.append("1" + item + "1")
                res.append("6" + item + "9")
                res.append("8" + item + "8")
                res.append("9" + item + "6")
                
            return res

# Used for testing
if __name__ == "__main__":
    test = Solution()
    low = "50"
    high = "100"
    test.strobogrammaticInRange(low, high)

# ------------------------------
# Summary: