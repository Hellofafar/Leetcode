# ------------------------------
# 190. Reverse Bits
# 
# Description:
# Reverse bits of a given 32 bits unsigned integer.
# Example:
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
#              return 964176192 represented in binary as 00111001011110000010100101000000.
# 
# Follow up:
# If this function is called many times, how would you optimize it?
# 
# Version: 1.0
# 06/10/18 by Jianfa
# ------------------------------

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        temp = bin(n)[2:]
        while len(temp) < 32:
            temp = "0" + temp
        
        return int(temp[::-1], 2)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# To reverse a string, use s[::-1]