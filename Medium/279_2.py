# ------------------------------
# 279. Perfect Squares
# 
# Description:
# 
# Version: 2.0
# 09/28/18 by Jianfa
# ------------------------------

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        leastNum = [0]
        
        # leastNum[1] = 1
        # leastNum[2] = least[1] + 1 = 2
        # leastNum[3] = least[2] + 1 = 3
        # leastNum[4] = min(least[4 - 1*1] + 1, least[4 - 2*2] + 1)
        # ...
        # leastNum[k] = min(least[k - j*j] + 1) for j * j <= k
        for i in range(1, n + 1):
            minimum = i
            j = 1
            while j * j <= i:
                minimum = min(minimum, leastNum[i - j * j] + 1)
                j += 1
            leastNum.append(minimum)
                
        return leastNum[-1]
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Static dynamic programming.