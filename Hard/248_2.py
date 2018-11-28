# ------------------------------
# 248. Strobogrammatic Number III
# 
# Description:
# 
# Version: 2.0
# 11/27/18 by Jianfa
# ------------------------------

class Solution:
    pairs = (('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6'))
    
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        count = [0]
        for length in range(len(low), len(high) + 1):
            char_str = [''] * length
            self.dfs(low, high, char_str, 0, length - 1, count)
        
        return count[0]
    
    def dfs(self, low, high, char_str, left, right, count):
        if left > right:
            if len(char_str) == len(low) and ''.join(char_str) < low or \
               len(char_str) == len(high) and ''.join(char_str) > high:
                return
            count[0] += 1
            return
        
        for p in self.pairs:
            char_str[left] = p[0]
            char_str[right] = p[1]
            if len(char_str) != 1 and char_str[0] == '0':  # Cannot start with '0' except number '0'
                continue
            
            if left == right and p[0] != p[1]:  # Middle one can only be '0', '1', '8' if there is only single middle number
                continue
            
            self.dfs(low, high, char_str, left+1, right-1, count)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/strobogrammatic-number-iii/discuss/67378/Concise-Java-Solution