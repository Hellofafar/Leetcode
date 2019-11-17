# ------------------------------
# 36. Valid Sudoku
# 
# Description:
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated 
# according to the following rules:
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# 
# Version: 2.0
# 11/16/19 by Jianfa
# ------------------------------

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in rows[i]:
                        return False
                    rows[i].add(num)
                    
                    if num in cols[j]:
                        return False
                    cols[j].add(num)
                    
                    grid_index = i // 3 * 3 + j // 3
                    if num in grids[grid_index]:
                        return False
                    grids[grid_index].add(num)
                    
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# One pass solution from https://leetcode.com/problems/valid-sudoku/solution/
# Easy to understand.
# Check the row, column and grid that the unit belongs to, use set for easy check.