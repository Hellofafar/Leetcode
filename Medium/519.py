# ------------------------------
# 519. Random Flip Matrix
# 
# Description:
# You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix 
# where all values are initially 0. Write a function flip which chooses a 0 value uniformly 
# t random, changes it to 1, and then returns the position [row.id, col.id] of that value. 
# Also, write a function reset which sets all values back to 0. Try to minimize the number of 
# calls to system's Math.random() and optimize the time and space complexity.
# 
# Note:
# 
# 1 <= n_rows, n_cols <= 10000
# 0 <= row.id < n_rows and 0 <= col.id < n_cols
# flip will not be called when the matrix has no 0 values left.
# the total number of calls to flip and reset will not exceed 1000.
# 
# Example 1:
# Input: 
# ["Solution","flip","flip","flip","flip"]
# [[2,3],[],[],[],[]]
# Output: [null,[0,1],[1,2],[1,0],[1,1]]
# 
# Example 2:
# Input: 
# ["Solution","flip","flip","reset","flip"]
# [[1,2],[],[],[],[]]
# Output: [null,[0,0],[0,1],null,[0,0]]
# 
# Explanation of Input Syntax:
# The input is two lists: the subroutines called and their arguments. Solution's constructor 
# has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always 
# wrapped with a list, even if there aren't any.
# 
# Version: 1.0
# 01/15/19 by Jianfa
# ------------------------------

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.row = n_rows
        self.col = n_cols
        self.total = self.row * self.col - 1
        self.map = dict()

    def flip(self) -> List[int]:
        r = random.randint(0, self.total) # random number
        x = self.map.get(r, r) # the actual number want to get
        self.map[r] = self.map.get(self.total, self.total) # if self.total is not selected this time, use map[r] to point to current self.total value
        self.total -= 1 # udpate self.total
        return [x // self.col, x % self.col]

    def reset(self) -> None:
        self.total = self.row * self.col - 1
        self.map.clear()    


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Solution from https://leetcode.com/problems/random-flip-matrix/discuss/154053/Java-AC-Solution-call-Least-times-of-Random.nextInt()-function
# Explanation see: https://leetcode.com/problems/random-flip-matrix/discuss/154053/Java-AC-Solution-call-Least-times-of-Random.nextInt()-function/159683