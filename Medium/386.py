# ------------------------------
# 386. Lexicographical Numbers
# 
# Description:
# Given an integer n, return 1 - n in lexicographical order.
# 
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
# 
# Version: 1.0
# 10/01/19 by Jianfa
# ------------------------------

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(i, n, res)
        
        return res
        
    def dfs(self, cur, n, res):
        if cur > n:
            return
        
        res.append(cur)
        for i in range(10):
            if cur*10 + i > n:
                return
            self.dfs(cur*10 + i, n, res)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution
# Follow idea from: https://leetcode.com/problems/lexicographical-numbers/discuss/86231/Simple-Java-DFS-Solution
# we just keep adding digit from 0 to 9 to every digit and make it a tree.
# Then we visit every node in pre-order. 
#        1        2        3    ...
#       /\        /\       /\
#    10 ...19  20...29  30...39   ....