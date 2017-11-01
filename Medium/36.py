# ------------------------------
# 36. Valid Sudoku
# 
# Description:
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# 
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# 
# Version: 1.0
# 11/01/17 by Jianfa
# ------------------------------

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for line in board:
            temp = line
            temp = list(filter(lambda x: x != '.', temp))
            if len(set(temp)) != len(temp):
                return False
            
        for cow in range(len(board)):
            temp = [board[l][cow] for l in range(len(board))]
            temp = list(filter(lambda x: x != '.', temp))
            if len(set(temp)) != len(temp):
                return False
                
        for l in range(3):
            for c in range(3):
                temp = board[l * 3][c * 3 : c * 3 + 3] + \
                       board[l * 3 + 1][c * 3 : c * 3 + 3] + \
                       board[l * 3 + 2][c * 3 : c * 3 + 3]
                temp = list(filter(lambda x: x != '.', temp))
                if len(set(temp)) != len(temp):
                    return False
        
        return True

# Used for test
if __name__ == "__main__":
    test = Solution()
    board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    
    print(test.isValidSudoku(board))

# ------------------------------
# Summary:
# O(3n) solution. I check every line at first, then every column, finally every sub-square. If there is 
# duplicate in a subset, then return False, else True.
# Another good idea from one of the best solution:
# Create three list includes 9 set() initially:
#   row = [set() for i in xrange(0, 9)]
#   col = [set() for i in xrange(0, 9)]
#   grid = [set() for i in xrange(0, 9)]
# Then traverse every unit, and check if it's in corresponding line/column/grid. 
# for i in range(9):
#   for j in range(9):
#       g = i / 3 * 3 + j / 3  # which grid does current unit belong to