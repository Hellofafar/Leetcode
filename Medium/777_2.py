# ------------------------------
# 777. Swap Adjacent in LR String
# 
# Description:
# 
# Version: 2.0
# 11/13/18 by Jianfa
# ------------------------------

import itertools
class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        i = 0
        j = 0
        for (i, s), (j, e) in itertools.zip_longest(
            ((i, x) for i, x in enumerate(start) if x != 'X'),
            ((j, y) for j, y in enumerate(end) if y != 'X'),
            fillvalue = (None, None)
        ):
            # if x != y: not solid
            # if (x == 'L' and i < j) or (x == 'R' and i > j): not accessible
            if s != e or (s == 'L' and i < j) or (s == 'R' and i > j):
                return False
            
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointer solution: https://leetcode.com/problems/swap-adjacent-in-lr-string/solution/