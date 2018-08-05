# ------------------------------
# 686. Repeated String Match
# 
# Description:
# 
# Version: 2.0
# 08/04/18 by Jianfa
# ------------------------------

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = (len(B) - 1) / len(A) + 1
        for i in range(2):
            if B in A * (times + i):
                return times + i
        
        return -1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 