# ------------------------------
# 118. Pascal's Triangle
# 
# Description:
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# 
# Version: 1.0
# 06/07/18 by Jianfa
# ------------------------------

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        
        pascal = [[1]]
        for i in range(1, numRows):
            last = pascal[i-1]
            curr = [1]
            for j in range(len(last) - 1):
                curr.append(last[j]+last[j+1])
            curr.append(1)
            pascal.append(curr)
        
        return pascal

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Calculate row by row.