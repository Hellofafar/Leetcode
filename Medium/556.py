# ------------------------------
# 556. Next Greater Element III
# 
# Description:
# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has 
# exactly the same digits existing in the integer n and is greater in value than n. If no 
# such positive 32-bit integer exists, you need to return -1.
# 
# Example 1:
# 
# Input: 12
# Output: 21
# 
# Example 2:
# 
# Input: 21
# Output: -1
# 
# Version: 1.0
# 01/22/20 by Jianfa
# ------------------------------

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nStr = list(str(n))
        
        # find index of the digit that is greater than its left digit
        index = len(nStr) - 1
        while index > 0:
            if nStr[index] > nStr[index-1]:
                break
            index -= 1
        
        if index == 0:
            # if nStr is sorted in descending order
            # no available result
            return -1
        
        x = nStr[index-1]
        smallest = index
        for j in range(smallest + 1, len(nStr)):
            if x < nStr[j] and nStr[j] <= nStr[smallest]:
                # find the digit j - 1 to swap with x
                smallest = j
        
        # swap the x and smallest digit on the right that is greater than x
        nStr[index-1], nStr[smallest] = nStr[smallest], nStr[index-1]
        
        # sort the digit on the right of nStr[index - 1]
        right = nStr[index:]
        right.sort()
        nStr[index:] = right
        
        res = int("".join(nStr))
        return res if res < pow(2, 31) else -1  

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from https://leetcode.com/problems/next-greater-element-iii/discuss/101824/Simple-Java-solution-(4ms)-with-explanation.
# 
# NOTE: 32-bit integer is considered as signed integer here, so largest number should be pow(2, 31) - 1