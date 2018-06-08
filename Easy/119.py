# ------------------------------
# 119. Pascal's Triangle II
# 
# Description:
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.
# Example:
# Input: 3
# Output: [1,3,3,1]
# 
# Follow up:
# Could you optimize your algorithm to use only O(k) extra space?
# 
# Version: 1.0
# 06/07/18 by Jianfa
# ------------------------------

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
            
        return row

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use the idea from https://leetcode.com/problems/pascals-triangle-ii/discuss/38467/Very-simple-Python-solution