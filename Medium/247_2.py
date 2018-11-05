# ------------------------------
# 247. Strobogrammatic Number II
# 
# Description:
# 
# Version: 2.0
# 11/04/18 by Jianfa
# ------------------------------

class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)
    
    # Helper function to get substrings
    # n is length of substring, m is length of required string
    def helper(self, n, m):
        if n == 0:
            return [""]
        
        elif n == 1:
            return ["0", "1", "8"]
        
        temp = self.helper(n-2, m)
        res = []
        for s in temp:
            if n != m:
                res.append("0" + s + "0")
            
            res.append("1" + s + "1")
            res.append("6" + s + "9")
            res.append("8" + s + "8")
            res.append("9" + s + "6")
            
        return res


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/strobogrammatic-number-ii/discuss/67280/AC-clean-Java-solution