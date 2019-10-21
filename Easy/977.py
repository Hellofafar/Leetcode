# ------------------------------
# 977. Squares of a Sorted Array
# 
# Description:
# Given an array of integers A sorted in non-decreasing order, return an array of the 
# squares of each number, also in sorted non-decreasing order.
# 
# Example 1:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# 
# Example 2:
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# Version: 1.0
# 10/21/19 by Jianfa
# ------------------------------

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return []
        
        if A[0] >= 0:
            return [x * x for x in A]
        
        else:
            left = 0
            right = len(A) - 1
            res = []
            while left <= right:
                ls = A[left] * A[left]
                rs = A[right] * A[right]
                if ls > rs:
                    res.append(ls)
                    left += 1
                else:
                    res.append(rs)
                    right -= 1
            
            res.reverse()
            return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointer solution from start and end respectively
# Append the larger one every time after compare the power of start number and power of end number