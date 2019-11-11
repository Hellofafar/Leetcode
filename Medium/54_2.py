# ------------------------------
# 54. Spiral Matrix
# 
# Description:
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# Version: 2.0
# 11/10/19 by Jianfa
# ------------------------------

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        M = len(matrix)
        N = len(matrix[0])
        seen = [[False] * N for _ in range(M)]
        res = []
        
        dr = [0, 1, 0, -1] # moving direction on row
        dc = [1, 0, -1, 0] # moving direction on column
        di = 0             # index of selecting dr and dc
        i, j = 0, 0
        for _ in range(M * N):
            res.append(matrix[i][j])
            seen[i][j] = True
            nr, nc = i + dr[di], j + dc[di] # next candidate position to go
            if 0 <= nr < M and 0 <= nc < N and not seen[nr][nc]:
                # if (nr, nc) in the bounds of matrix and not visited before
                i, j = nr, nc
            else:
                di = (di + 1) % 4
                i, j = i + dr[di], j + dc[di] # get the correct position to go
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/spiral-matrix/solution/ Approach 1
# 
# Key idea is to simulate moving from outside to inside, using dr and dc to control
# direction, using seen to indicate whether the unit was visited.
# 
# O(MN) time O(MN) space