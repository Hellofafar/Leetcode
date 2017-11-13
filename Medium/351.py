# ------------------------------
# 351. Android Unlock Patterns
# 
# Description:
# https://leetcode.com/problems/android-unlock-patterns/description/
# 
# Version: 1.0
# 11/11/17 by Jianfa
# ------------------------------

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        candidate = [i for i in range(1,10)]
        neighbour = {1:[2,4,5,6,8], 2:[1,3,4,5,6,7,9], 3:[2,4,5,6,8], \
                     4:[1,2,3,5,7,8,9], 5:[1,2,3,4,6,7,8,9], 6:[1,2,3,5,7,8,9], \
                     7:[2,4,5,6,8], 8:[1,3,4,5,6,7,9], 9:[2,4,5,6,8]}
        for i in range(1,10):
            curr = [i]
            rest = [j for j in candidate if j != i]
            for targetLen in range(m, n+1):
                res = self.backtrack(res, curr, rest, targetLen, neighbour)
        
        return res
                
    def backtrack(self, res, curr, rest, targetLen, neighbour):
        currLen = len(curr)
        if currLen == targetLen:
            res += 1
            return res
            
        temp_rest = [x for x in rest]  # It's necessary so that when operating rest, won't affect iteration
        for i in temp_rest:
            if i in neighbour[curr[-1]] or (curr[-1] + i) / 2 in curr:
                curr.append(i)
                rest.remove(i)
                res = self.backtrack(res, curr, rest, targetLen, neighbour)
                rest.append(i)
                curr.remove(i)
            
        return res

# ------------------------------
# Summary:
# I use backtrack method with dictionary, traverse every possible situation. Complexity is N^k